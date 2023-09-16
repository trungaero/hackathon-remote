import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QStackedLayout, QMainWindow,  QStackedLayout, QWidget, QApplication # add this import
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QKeyEvent

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

import traceback, sys
from communication import Commands, Mode, Direction, list_ports, ComPort
from model import AppState
import time
from estimator import Navigator


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)
    data = pyqtSignal(object)



class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.is_active = True
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress
        self.kwargs['data'] = self.signals.data

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            while self.is_active:
                result = self.fn(*self.args, **self.kwargs)

            if not self.is_active:
                print('exiting.')
                return
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)

        # some states
        self.appstate = AppState()

        # mapping keys to slots
        self.key_mapping = self.load_key_mapping()

        # initialize com port
        self.com = ComPort('')
        self.nav = Navigator()

        # plot
        self.graphWidget = pg.PlotWidget(self.frame)
        self.graphWidget.setXRange(-50, 50, padding=0)
        self.graphWidget.setYRange(-50, 50, padding=0)
        self.graphWidget.setGeometry(12, 20, 579, 484)
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=True, y=True, alpha=0.2)
        # test background image
        # make plot with a line drawn in
        import numpy as np
        # add an image, scaled
        img = pg.ImageItem(np.random.normal(size=(100,100)))
        self.graphWidget.addItem(img)
        self.arrow = pg.ArrowItem(pos=(0,0), angle=self.appstate.theta + 90, brush=(255, 0, 0))
        self.graphWidget.addItem(self.arrow)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.appstate.xtrace, self.appstate.ytrace, pen=pen)


        # Create a tooltip item
        # self.tooltip = QGraphicsTextItem()
        # self.tooltip.setFlag(QGraphicsTextItem.ItemIgnoresTransformations)
        # self.tooltip.setFlag(QGraphicsTextItem.ItemIsSelectable)
        # self.tooltip.setDefaultTextColor(Qt.white)
        # self.tooltip.setPos(0, 0)
        # self.graphWidget.scene().sigSceneMousedMoved.connect(self.updatetooltip)

        # start thread pool
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.worker = Worker(self.check_com_ports)
        self.worker.signals.data.connect(self.display_com_ports)
        self.worker.setAutoDelete(True)
        self.threadpool.start(self.worker)

        self.worker1 = Worker(self.update_appstate, self.com)
        # self.worker.signals.data.connect(self.display_com_ports)
        self.worker1.signals.data.connect(self.update_plot_data)
        self.worker1.setAutoDelete(True)
        self.threadpool.start(self.worker1)

        # default page
        self.stackedWidget.setCurrentIndex(0)
        self.radioBtnConnection.setChecked(True)

        # signals to slots    
        self.radioBtnConnection.toggled.connect(self.toggle_connection_view)
        self.radioBtnControl.toggled.connect(self.toggle_control_view)
        self.pushBtnComConnect.clicked.connect(self.toggle_com_connection)

        # set buttons checkable
        self.pushBtnMoveForward.clicked.connect(self.send_command)
        self.pushBtnMoveBackward.clicked.connect(self.send_command)
        self.pushBtnRotateLeft.clicked.connect(self.send_command)
        self.pushBtnRotateRight.clicked.connect(self.send_command)
        # self.pushBtnPullArm.clicked.connect(self.send_command)
        self.pushBtnSetArm.clicked.connect(self.set_arm)
        self.pushBtnExtendFoot.clicked.connect(self.change_foot_length)
        self.pushBtnContractFoot.clicked.connect(self.change_foot_length)
        self.verticalSlider.valueChanged.connect(self.change_foot_length_slider)
        self.pushBtnResetFoot.clicked.connect(self.reset_foot_length)
        # self.pushBtnResetArm.clicked.connect(self.reset_arm)
        self.pushBtnSetSpeed.clicked.connect(self.set_speed)
        self.pushBtnLcd.clicked.connect(self.display_lcd)
        self.pushBtnResetPos.clicked.connect(self.reset_position)


    def load_key_mapping(self):
        return {
            Qt.Key_I: (self.pushBtnMoveForward, Commands.MOVE, Direction.FORWARD),
            Qt.Key_K: (self.pushBtnMoveBackward, Commands.MOVE, Direction.BACKWARD),
            Qt.Key_J: (self.pushBtnRotateLeft, Commands.MOVE, Direction.RLEFT),
            Qt.Key_L: (self.pushBtnRotateRight, Commands.MOVE, Direction.RRIGHT),
            Qt.Key_Q: (self.pushBtnExtendFoot, Commands.SET_FOOT),
            Qt.Key_A: (self.pushBtnContractFoot, Commands.SET_FOOT),
            # Qt.Key_E: (self.pushBtnPullArm, Commands.SET_ARM, ArmDirection.PULL),
            # Qt.Key_D: (self.pushBtnPushArm, Commands.SET_ARM, ArmDirection.PUSH),
            Qt.Key_D: (self.pushBtnSetArm, Commands.SET_ARM),
        }


    def display_com_ports(self, ports):
        if sorted(ports) != sorted([self.comboBoxComPort.itemText(i) for i in range(self.comboBoxComPort.count())]):
            self.comboBoxComPort.clear()
            self.comboBoxComPort.addItems(ports)

    def toggle_connection_view(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(0)

    def toggle_control_view(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(1)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()

        # highlight keys
        if key in self.key_mapping:
            highlight_button(self.key_mapping[key][0])
            self.key_mapping[key][0].clicked.emit()
        
        # sending modes via keyboard
        mode_keys = {
            Qt.Key_0: (0, self.radioBtnMode0),
            Qt.Key_1: (1, self.radioBtnMode1),
            Qt.Key_2: (2, self.radioBtnMode2),
            Qt.Key_3: (3, self.radioBtnMode3),
            Qt.Key_4: (4, self.radioBtnMode4),
            Qt.Key_5: (5, self.radioBtnMode5),
            Qt.Key_6: (6, self.radioBtnMode6),
            Qt.Key_7: (7, self.radioBtnMode7),
        }
        if event.key() in mode_keys and event.modifiers() == Qt.ControlModifier:
            # set mode checked on GUI 
            mode_keys[event.key()][1].setChecked(True)
            self.com.send(Commands.SET_MODE, mode_keys[event.key()][0])
            

    def send_command(self):
        sender_button = self.sender() 
        for key, btn in self.key_mapping.items():
            if sender_button is btn[0]:
                self.com.send(*self.key_mapping[key][1:])

    def keyReleaseEvent(self, event: QKeyEvent):
        key = event.key()
        if key in self.key_mapping:
            unhighlight_button(self.key_mapping[key][0])

    def toggle_com_connection(self):
        self.com.device_name = self.comboBoxComPort.currentText()
        if self.pushBtnComConnect.text() == "Connect":
            if self.com.connect():
                self.pushBtnComConnect.setText("Disconnect")
        else:
            self.com.close()
            self.pushBtnComConnect.setText("Connect")

    def change_foot_length(self):
        sender_button = self.sender() 
        if sender_button is self.pushBtnExtendFoot:
            self.appstate.foot_len += self.appstate.foot_increment
        elif sender_button is self.pushBtnContractFoot:
            self.appstate.foot_len -= self.appstate.foot_increment
        self.verticalSlider.setValue(self.appstate.foot_len)
        self.com.send(Commands.SET_FOOT, self.appstate.foot_len)

    def change_foot_length_slider(self):
        self.appstate.foot_len = self.verticalSlider.value()
        self.com.send(Commands.SET_FOOT, self.appstate.foot_len)

    def set_arm(self):
        arm_cnt = int(self.spinBoxArmCount.value())
        arm_distance = int(self.spinBoxArmDistance.value())
        self.com.send(Commands.SET_ARM, str(arm_cnt * arm_distance))

    def reset_foot_length(self):
        self.appstate.foot_len = 0
        self.verticalSlider.setValue(self.appstate.foot_len)
        self.com.send(Commands.SET_FOOT, self.appstate.foot_len)

    # def reset_arm(self):
    #     self.com.send(Commands.SET_ARM, ArmDirection.NULL)

    def set_speed(self):
        self.com.send(Commands.SET_SPEED, int(self.spinBoxSpeed.value()))

    def display_lcd(self):
        self.com.send(Commands.SET_DISP, int(self.spinBoxLcd.value()))

    def check_com_ports(self, *args, **kwargs):
        ports = list_ports()
        kwargs['data'].emit(ports)
        time.sleep(0.5)

    def update_appstate(self, *args, **kwargs):
        packet = self.com.recv_data()
        if packet:
            self.nav.update(packet)
            self.appstate.x_current = int(self.nav.x)
            self.appstate.y_current = int(self.nav.y)
            self.appstate.theta = int(self.nav.the)
            kwargs['data'].emit(packet)

    def update_plot_data(self, data):
        self.data_line.setData(self.appstate.xtrace, self.appstate.ytrace)
        self.arrow.setPos(self.appstate.x_current, self.appstate.y_current)
        self.arrow.setStyle(angle=self.appstate.theta + 90)

    def reset_position(self):
        x0 = int(self.lineEditResetX.text())
        y0 = int(self.lineEditResetY.text())
        the0 = int(self.lineEditResetThe.text())

        self.nav.reset(x=x0, y=y0, the=the0)
        self.appstate.reset_trace()
        self.appstate.x_current = int(self.nav.x)
        self.appstate.y_current = int(self.nav.y)
        self.data_line.setData(self.appstate.xtrace, self.appstate.ytrace)
        self.arrow.setPos(self.appstate.x_current, self.appstate.y_current)
        self.arrow.setStyle(angle=self.appstate.theta + 90)

    def closeEvent(self, event):
        print('preparing to exit...')
        self.worker.is_active = False
        self.worker1.is_active = False
        # Close the application
        self.close()


def highlight_button(btn):
    btn.setStyleSheet("background: yellow;")


def unhighlight_button(btn):
    btn.setStyleSheet("")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())