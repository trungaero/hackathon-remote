# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1403, 905)
        MainWindow.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: #E0E0E0;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.radioBtnConnection = QtWidgets.QRadioButton(self.frame_2)
        self.radioBtnConnection.setObjectName("radioBtnConnection")
        self.verticalLayout.addWidget(self.radioBtnConnection)
        self.radioBtnControl = QtWidgets.QRadioButton(self.frame_2)
        self.radioBtnControl.setObjectName("radioBtnControl")
        self.verticalLayout.addWidget(self.radioBtnControl)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setEnabled(True)
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBoxComPort = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxComPort.setObjectName("comboBoxComPort")
        self.horizontalLayout_3.addWidget(self.comboBoxComPort)
        self.pushBtnComConnect = QtWidgets.QPushButton(self.groupBox)
        self.pushBtnComConnect.setObjectName("pushBtnComConnect")
        self.horizontalLayout_3.addWidget(self.pushBtnComConnect)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditUrlCamera = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditUrlCamera.setObjectName("lineEditUrlCamera")
        self.horizontalLayout_2.addWidget(self.lineEditUrlCamera)
        self.pushBtnTestCamConnect = QtWidgets.QPushButton(self.groupBox_4)
        self.pushBtnTestCamConnect.setObjectName("pushBtnTestCamConnect")
        self.horizontalLayout_2.addWidget(self.pushBtnTestCamConnect)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(500, 100))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioBtnMode2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioBtnMode2.setObjectName("radioBtnMode2")
        self.gridLayout_3.addWidget(self.radioBtnMode2, 1, 2, 1, 1)
        self.radioBtnMode7 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioBtnMode7.setObjectName("radioBtnMode7")
        self.gridLayout_3.addWidget(self.radioBtnMode7, 3, 3, 1, 1)
        self.radioBtnMode4 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioBtnMode4.setObjectName("radioBtnMode4")
        self.gridLayout_3.addWidget(self.radioBtnMode4, 3, 0, 1, 1)
        self.radioBtnMode5 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioBtnMode5.setObjectName("radioBtnMode5")
        self.gridLayout_3.addWidget(self.radioBtnMode5, 3, 1, 1, 1)
        self.radioBtnMode0 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioBtnMode0.setObjectName("radioBtnMode0")
        self.gridLayout_3.addWidget(self.radioBtnMode0, 1, 0, 1, 1)
        self.radioBtnMode6 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioBtnMode6.setObjectName("radioBtnMode6")
        self.gridLayout_3.addWidget(self.radioBtnMode6, 3, 2, 1, 1)
        self.radioBtnMode3 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioBtnMode3.setObjectName("radioBtnMode3")
        self.gridLayout_3.addWidget(self.radioBtnMode3, 1, 3, 1, 1)
        self.radioBtnMode1 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioBtnMode1.setObjectName("radioBtnMode1")
        self.gridLayout_3.addWidget(self.radioBtnMode1, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 5, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 400))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(579, 484))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.pushBtnNextMap = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtnNextMap.sizePolicy().hasHeightForWidth())
        self.pushBtnNextMap.setSizePolicy(sizePolicy)
        self.pushBtnNextMap.setObjectName("pushBtnNextMap")
        self.verticalLayout_3.addWidget(self.pushBtnNextMap)
        self.pushBtnPrevMap = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtnPrevMap.sizePolicy().hasHeightForWidth())
        self.pushBtnPrevMap.setSizePolicy(sizePolicy)
        self.pushBtnPrevMap.setObjectName("pushBtnPrevMap")
        self.verticalLayout_3.addWidget(self.pushBtnPrevMap)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.frame_3 = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 3, 0, 1, 1)
        self.lineEditSetThe = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditSetThe.setObjectName("lineEditSetThe")
        self.gridLayout_4.addWidget(self.lineEditSetThe, 2, 7, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 3, 6, 1, 1)
        self.lineEditSetTargetX = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditSetTargetX.setObjectName("lineEditSetTargetX")
        self.gridLayout_4.addWidget(self.lineEditSetTargetX, 3, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 4, 1, 1)
        self.pushBtnResetPos = QtWidgets.QPushButton(self.frame_3)
        self.pushBtnResetPos.setObjectName("pushBtnResetPos")
        self.gridLayout_4.addWidget(self.pushBtnResetPos, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 2, 6, 1, 1)
        self.pushBtnSetPos = QtWidgets.QPushButton(self.frame_3)
        self.pushBtnSetPos.setObjectName("pushBtnSetPos")
        self.gridLayout_4.addWidget(self.pushBtnSetPos, 2, 0, 1, 1)
        self.lineEditSetPosY = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSetPosY.sizePolicy().hasHeightForWidth())
        self.lineEditSetPosY.setSizePolicy(sizePolicy)
        self.lineEditSetPosY.setObjectName("lineEditSetPosY")
        self.gridLayout_4.addWidget(self.lineEditSetPosY, 2, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 1, 1, 1)
        self.lineEditSetPosX = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSetPosX.sizePolicy().hasHeightForWidth())
        self.lineEditSetPosX.setSizePolicy(sizePolicy)
        self.lineEditSetPosX.setObjectName("lineEditSetPosX")
        self.gridLayout_4.addWidget(self.lineEditSetPosX, 2, 3, 1, 1)
        self.lineEditSetTargetY = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditSetTargetY.setObjectName("lineEditSetTargetY")
        self.gridLayout_4.addWidget(self.lineEditSetTargetY, 3, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 1, 1, 1)
        self.lineEditSetTargetThe = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditSetTargetThe.setObjectName("lineEditSetTargetThe")
        self.gridLayout_4.addWidget(self.lineEditSetTargetThe, 3, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 3, 4, 1, 1)
        self.lineEditResetX = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditResetX.setObjectName("lineEditResetX")
        self.gridLayout_4.addWidget(self.lineEditResetX, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 1, 4, 1, 1)
        self.lineEditResetY = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditResetY.setObjectName("lineEditResetY")
        self.gridLayout_4.addWidget(self.lineEditResetY, 1, 5, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 6, 1, 1)
        self.lineEditResetThe = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditResetThe.setObjectName("lineEditResetThe")
        self.gridLayout_4.addWidget(self.lineEditResetThe, 1, 7, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 0, 1, 1)
        self.spinBoxLcd = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBoxLcd.setMinimum(1)
        self.spinBoxLcd.setMaximum(4)
        self.spinBoxLcd.setObjectName("spinBoxLcd")
        self.gridLayout_2.addWidget(self.spinBoxLcd, 1, 1, 1, 1)
        self.pushBtnLcd = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtnLcd.sizePolicy().hasHeightForWidth())
        self.pushBtnLcd.setSizePolicy(sizePolicy)
        self.pushBtnLcd.setMinimumSize(QtCore.QSize(150, 0))
        self.pushBtnLcd.setObjectName("pushBtnLcd")
        self.gridLayout_2.addWidget(self.pushBtnLcd, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_6, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBoxSpeed = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxSpeed.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxSpeed.setMaximum(100)
        self.spinBoxSpeed.setObjectName("spinBoxSpeed")
        self.gridLayout.addWidget(self.spinBoxSpeed, 1, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.pushBtnContractFoot = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtnContractFoot.sizePolicy().hasHeightForWidth())
        self.pushBtnContractFoot.setSizePolicy(sizePolicy)
        self.pushBtnContractFoot.setMinimumSize(QtCore.QSize(100, 0))
        self.pushBtnContractFoot.setObjectName("pushBtnContractFoot")
        self.gridLayout.addWidget(self.pushBtnContractFoot, 2, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 1, 10, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 1, 3, 1, 1)
        self.pushBtnPullArm = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtnPullArm.setObjectName("pushBtnPullArm")
        self.gridLayout.addWidget(self.pushBtnPullArm, 1, 8, 1, 1)
        self.pushBtnExtendFoot = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtnExtendFoot.sizePolicy().hasHeightForWidth())
        self.pushBtnExtendFoot.setSizePolicy(sizePolicy)
        self.pushBtnExtendFoot.setMinimumSize(QtCore.QSize(100, 0))
        self.pushBtnExtendFoot.setObjectName("pushBtnExtendFoot")
        self.gridLayout.addWidget(self.pushBtnExtendFoot, 1, 4, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy)
        self.verticalSlider.setMinimumSize(QtCore.QSize(0, 50))
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 1, 5, 2, 1)
        self.pushBtnPushArm = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtnPushArm.setObjectName("pushBtnPushArm")
        self.gridLayout.addWidget(self.pushBtnPushArm, 2, 8, 1, 1)
        self.pushBtnSetSpeed = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtnSetSpeed.setObjectName("pushBtnSetSpeed")
        self.gridLayout.addWidget(self.pushBtnSetSpeed, 2, 2, 1, 1)
        self.pushBtnResetFoot = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtnResetFoot.setObjectName("pushBtnResetFoot")
        self.gridLayout.addWidget(self.pushBtnResetFoot, 0, 4, 1, 1)
        self.pushBtnResetArm = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtnResetArm.setObjectName("pushBtnResetArm")
        self.gridLayout.addWidget(self.pushBtnResetArm, 0, 8, 1, 1)
        self.pushBtnMoveForward = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtnMoveForward.sizePolicy().hasHeightForWidth())
        self.pushBtnMoveForward.setSizePolicy(sizePolicy)
        self.pushBtnMoveForward.setMinimumSize(QtCore.QSize(100, 0))
        self.pushBtnMoveForward.setObjectName("pushBtnMoveForward")
        self.gridLayout.addWidget(self.pushBtnMoveForward, 0, 12, 1, 1)
        self.pushBtnRotateLeft = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtnRotateLeft.sizePolicy().hasHeightForWidth())
        self.pushBtnRotateLeft.setSizePolicy(sizePolicy)
        self.pushBtnRotateLeft.setMinimumSize(QtCore.QSize(100, 0))
        self.pushBtnRotateLeft.setObjectName("pushBtnRotateLeft")
        self.gridLayout.addWidget(self.pushBtnRotateLeft, 1, 11, 1, 1)
        self.pushBtnRotateRight = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtnRotateRight.sizePolicy().hasHeightForWidth())
        self.pushBtnRotateRight.setSizePolicy(sizePolicy)
        self.pushBtnRotateRight.setMinimumSize(QtCore.QSize(100, 0))
        self.pushBtnRotateRight.setObjectName("pushBtnRotateRight")
        self.gridLayout.addWidget(self.pushBtnRotateRight, 1, 13, 1, 1)
        self.pushBtnMoveBackward = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtnMoveBackward.setObjectName("pushBtnMoveBackward")
        self.gridLayout.addWidget(self.pushBtnMoveBackward, 1, 12, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout)
        self.gridLayout_5.addWidget(self.groupBox_2, 3, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_2)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stackedWidget)
        self.horizontalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1403, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioBtnConnection.setText(_translate("MainWindow", "Connection"))
        self.radioBtnControl.setText(_translate("MainWindow", "Control"))
        self.groupBox.setTitle(_translate("MainWindow", "COM"))
        self.label.setText(_translate("MainWindow", "Port"))
        self.pushBtnComConnect.setText(_translate("MainWindow", "Connect"))
        self.groupBox_4.setTitle(_translate("MainWindow", "CAMERA"))
        self.label_2.setText(_translate("MainWindow", "URL"))
        self.pushBtnTestCamConnect.setText(_translate("MainWindow", "Connect"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Modes"))
        self.radioBtnMode2.setText(_translate("MainWindow", "2"))
        self.radioBtnMode7.setText(_translate("MainWindow", "7"))
        self.radioBtnMode4.setText(_translate("MainWindow", "4"))
        self.radioBtnMode5.setText(_translate("MainWindow", "5"))
        self.radioBtnMode0.setText(_translate("MainWindow", "0"))
        self.radioBtnMode6.setText(_translate("MainWindow", "6"))
        self.radioBtnMode3.setText(_translate("MainWindow", "3"))
        self.radioBtnMode1.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "Hold Ctrl + 0,1.."))
        self.groupBox_3.setTitle(_translate("MainWindow", "Views"))
        self.pushBtnNextMap.setText(_translate("MainWindow", "Next Map >>"))
        self.pushBtnPrevMap.setText(_translate("MainWindow", "<< Prev Map"))
        self.pushButton_5.setText(_translate("MainWindow", "Set target"))
        self.label_10.setText(_translate("MainWindow", "The"))
        self.label_7.setText(_translate("MainWindow", "X"))
        self.label_6.setText(_translate("MainWindow", "Y"))
        self.pushBtnResetPos.setText(_translate("MainWindow", "Reset"))
        self.label_9.setText(_translate("MainWindow", "The"))
        self.pushBtnSetPos.setText(_translate("MainWindow", "Set Position"))
        self.label_11.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "X"))
        self.label_8.setText(_translate("MainWindow", "Y"))
        self.lineEditResetX.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Y"))
        self.lineEditResetY.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "The"))
        self.lineEditResetThe.setText(_translate("MainWindow", "0"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Display"))
        self.pushBtnLcd.setText(_translate("MainWindow", "LCD"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Motor controls"))
        self.label_5.setText(_translate("MainWindow", "Set speed (%)"))
        self.pushBtnContractFoot.setText(_translate("MainWindow", "Contract (A)"))
        self.pushBtnPullArm.setText(_translate("MainWindow", "Pull (E)"))
        self.pushBtnExtendFoot.setText(_translate("MainWindow", "Extend (Q)"))
        self.pushBtnPushArm.setText(_translate("MainWindow", "Push (D)"))
        self.pushBtnSetSpeed.setText(_translate("MainWindow", "SET"))
        self.pushBtnResetFoot.setText(_translate("MainWindow", "Reset"))
        self.pushBtnResetArm.setText(_translate("MainWindow", "Reset"))
        self.pushBtnMoveForward.setText(_translate("MainWindow", "Forward"))
        self.pushBtnRotateLeft.setText(_translate("MainWindow", "Left"))
        self.pushBtnRotateRight.setText(_translate("MainWindow", "Right"))
        self.pushBtnMoveBackward.setText(_translate("MainWindow", "Backward"))
