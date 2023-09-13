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
from communication import Commands, Mode, Direction, ArmDirection, list_ports, ComPort
from model import AppState
import time
import re


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

        # plot
        self.graphWidget = pg.PlotWidget(self.frame)
        self.graphWidget.setGeometry(0, 0, 441, 368)
        self.graphWidget.setBackground('w')
        self.x = [0]
        self.y = [0]
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        # start thread pool
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.worker = Worker(self.check_com_ports)
        self.worker.signals.data.connect(self.display_com_ports)
        self.worker.setAutoDelete(True)
        self.threadpool.start(self.worker)

        self.worker1 = Worker(self.test_com, self.com)
        # self.worker.signals.data.connect(self.display_com_ports)
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
        self.pushBtnPullArm.clicked.connect(self.send_command)
        self.pushBtnPushArm.clicked.connect(self.send_command)
        self.pushBtnExtendFoot.clicked.connect(self.change_foot_length)
        self.pushBtnContractFoot.clicked.connect(self.change_foot_length)
        self.verticalSlider.valueChanged.connect(self.change_foot_length_slider)
        self.pushBtnResetFoot.clicked.connect(self.reset_foot_length)
        self.pushBtnResetArm.clicked.connect(self.reset_arm)
        self.pushBtnSetSpeed.clicked.connect(self.set_speed)
        self.pushBtnLcd.clicked.connect(self.display_lcd)

        self.worker1.signals.data.connect(self.update_plot_data)



    def load_key_mapping(self):
        return {
            Qt.Key_I: (self.pushBtnMoveForward, Commands.MOVE, Direction.FORWARD),
            Qt.Key_K: (self.pushBtnMoveBackward, Commands.MOVE, Direction.BACKWARD),
            Qt.Key_J: (self.pushBtnRotateLeft, Commands.MOVE, Direction.RLEFT),
            Qt.Key_L: (self.pushBtnRotateRight, Commands.MOVE, Direction.RRIGHT),
            Qt.Key_Q: (self.pushBtnExtendFoot, Commands.SET_FOOT),
            Qt.Key_A: (self.pushBtnContractFoot, Commands.SET_FOOT),
            Qt.Key_E: (self.pushBtnPullArm, Commands.SET_ARM, ArmDirection.PULL),
            Qt.Key_D: (self.pushBtnPushArm, Commands.SET_ARM, ArmDirection.PUSH),
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

    def reset_foot_length(self):
        self.appstate.foot_len = 0
        self.verticalSlider.setValue(self.appstate.foot_len)
        self.com.send(Commands.SET_FOOT, self.appstate.foot_len)

    def reset_arm(self):
        self.com.send(Commands.SET_ARM, ArmDirection.NULL)

    def set_speed(self):
        self.com.send(Commands.SET_SPEED, int(self.spinBoxSpeed.value()))

    def display_lcd(self):
        self.com.send(Commands.SET_DISP, int(self.spinBoxLcd.value()))

    def check_com_ports(self, *args, **kwargs):
        ports = list_ports()
        kwargs['data'].emit(ports)
        time.sleep(0.5)

    def test_com(self, *args, **kwargs):
        data = self.com.recv()
        if data:
            # print(data)
            m = re.findall('(?<=Value:)(\d+),(\d+)', data)
            xs = self.x
            ys = self.y
            print(m)
            if len(m)>0:
                x, y = (m[0][0], m[0][1])
                xs.append(int(x))
                ys.append(int(y))
                if len(xs)>100:
                    kwargs['data'].emit((xs[-100:], ys[-100:]))
                else:
                    kwargs['data'].emit((xs, ys))
        # time.sleep(0.05)

    def update_plot_data(self, data):
        self.data_line.setData(data[0], data[1])

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