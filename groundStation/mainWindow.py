# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sat Feb 23 08:55:27 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1018, 678)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/Images/headerImage.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 8)
        self.groupBox_17 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_17.setObjectName(_fromUtf8("groupBox_17"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.groupBox_17)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.motor0Slider = QtGui.QSlider(self.groupBox_17)
        self.motor0Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor0Slider.setObjectName(_fromUtf8("motor0Slider"))
        self.horizontalLayout_18.addWidget(self.motor0Slider)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        self.verticalLayout_19.addLayout(self.horizontalLayout_18)
        self.motor0SpinBox = QtGui.QSpinBox(self.groupBox_17)
        self.motor0SpinBox.setObjectName(_fromUtf8("motor0SpinBox"))
        self.verticalLayout_19.addWidget(self.motor0SpinBox)
        self.gridLayout_5.addWidget(self.groupBox_17, 1, 0, 4, 1)
        self.groupBox_18 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_18.setObjectName(_fromUtf8("groupBox_18"))
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.groupBox_18)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem2)
        self.motor1Slider = QtGui.QSlider(self.groupBox_18)
        self.motor1Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor1Slider.setObjectName(_fromUtf8("motor1Slider"))
        self.horizontalLayout_19.addWidget(self.motor1Slider)
        spacerItem3 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem3)
        self.verticalLayout_20.addLayout(self.horizontalLayout_19)
        self.motor1SpinBox = QtGui.QSpinBox(self.groupBox_18)
        self.motor1SpinBox.setObjectName(_fromUtf8("motor1SpinBox"))
        self.verticalLayout_20.addWidget(self.motor1SpinBox)
        self.gridLayout_5.addWidget(self.groupBox_18, 1, 1, 4, 1)
        self.groupBox_19 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_19.setObjectName(_fromUtf8("groupBox_19"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.groupBox_19)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        spacerItem4 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem4)
        self.motor2Slider = QtGui.QSlider(self.groupBox_19)
        self.motor2Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor2Slider.setObjectName(_fromUtf8("motor2Slider"))
        self.horizontalLayout_20.addWidget(self.motor2Slider)
        spacerItem5 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem5)
        self.verticalLayout_21.addLayout(self.horizontalLayout_20)
        self.motor2SpinBox = QtGui.QSpinBox(self.groupBox_19)
        self.motor2SpinBox.setObjectName(_fromUtf8("motor2SpinBox"))
        self.verticalLayout_21.addWidget(self.motor2SpinBox)
        self.gridLayout_5.addWidget(self.groupBox_19, 1, 2, 4, 1)
        self.groupBox_20 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_20.setObjectName(_fromUtf8("groupBox_20"))
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.groupBox_20)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        spacerItem6 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem6)
        self.motor3Slider = QtGui.QSlider(self.groupBox_20)
        self.motor3Slider.setOrientation(QtCore.Qt.Vertical)
        self.motor3Slider.setObjectName(_fromUtf8("motor3Slider"))
        self.horizontalLayout_21.addWidget(self.motor3Slider)
        spacerItem7 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem7)
        self.verticalLayout_22.addLayout(self.horizontalLayout_21)
        self.motor3SpinBox = QtGui.QSpinBox(self.groupBox_20)
        self.motor3SpinBox.setObjectName(_fromUtf8("motor3SpinBox"))
        self.verticalLayout_22.addWidget(self.motor3SpinBox)
        self.gridLayout_5.addWidget(self.groupBox_20, 1, 3, 4, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_5.addWidget(self.line, 1, 4, 2, 1)
        self.groupBox_21 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_21.setObjectName(_fromUtf8("groupBox_21"))
        self.verticalLayout_23 = QtGui.QVBoxLayout(self.groupBox_21)
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        spacerItem8 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem8)
        self.masterMotorSlider = QtGui.QSlider(self.groupBox_21)
        self.masterMotorSlider.setOrientation(QtCore.Qt.Vertical)
        self.masterMotorSlider.setObjectName(_fromUtf8("masterMotorSlider"))
        self.horizontalLayout_22.addWidget(self.masterMotorSlider)
        spacerItem9 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem9)
        self.verticalLayout_23.addLayout(self.horizontalLayout_22)
        self.masterMotorSpinBox = QtGui.QSpinBox(self.groupBox_21)
        self.masterMotorSpinBox.setObjectName(_fromUtf8("masterMotorSpinBox"))
        self.verticalLayout_23.addWidget(self.masterMotorSpinBox)
        self.gridLayout_5.addWidget(self.groupBox_21, 1, 5, 4, 1)
        self.groupBox_11 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_2 = QtGui.QLabel(self.groupBox_11)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_10.addWidget(self.label_2)
        self.ipAddressEdit = QtGui.QLineEdit(self.groupBox_11)
        self.ipAddressEdit.setObjectName(_fromUtf8("ipAddressEdit"))
        self.verticalLayout_10.addWidget(self.ipAddressEdit)
        self.label_3 = QtGui.QLabel(self.groupBox_11)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_10.addWidget(self.label_3)
        self.portEdit = QtGui.QLineEdit(self.groupBox_11)
        self.portEdit.setObjectName(_fromUtf8("portEdit"))
        self.verticalLayout_10.addWidget(self.portEdit)
        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 2, 1)
        self.line_2 = QtGui.QFrame(self.groupBox_11)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 0, 1, 2, 1)
        self.connectButton = QtGui.QPushButton(self.groupBox_11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.gridLayout_4.addWidget(self.connectButton, 0, 2, 1, 1)
        self.disconnectButton = QtGui.QPushButton(self.groupBox_11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy)
        self.disconnectButton.setObjectName(_fromUtf8("disconnectButton"))
        self.gridLayout_4.addWidget(self.disconnectButton, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_11, 1, 6, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox_6)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBox)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout_5.addWidget(self.groupBox_6, 1, 7, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.xAccelEdit = QtGui.QLineEdit(self.groupBox_8)
        self.xAccelEdit.setStyleSheet(_fromUtf8("background-color: rgb(6, 5, 4);\n"
"color: rgb(64, 181, 64);\n"
"font: 9pt \"Monospace\";"))
        self.xAccelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.xAccelEdit.setObjectName(_fromUtf8("xAccelEdit"))
        self.gridLayout.addWidget(self.xAccelEdit, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_8)
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.yAccelEdit = QtGui.QLineEdit(self.groupBox_9)
        self.yAccelEdit.setStyleSheet(_fromUtf8("background-color: rgb(6, 5, 4);\n"
"color: rgb(64, 181, 64);\n"
"font: 9pt \"Monospace\";"))
        self.yAccelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.yAccelEdit.setObjectName(_fromUtf8("yAccelEdit"))
        self.gridLayout_2.addWidget(self.yAccelEdit, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_9)
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.zAccelEdit = QtGui.QLineEdit(self.groupBox_10)
        self.zAccelEdit.setStyleSheet(_fromUtf8("background-color: rgb(6, 5, 4);\n"
"color: rgb(64, 181, 64);\n"
"font: 9pt \"Monospace\";"))
        self.zAccelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.zAccelEdit.setObjectName(_fromUtf8("zAccelEdit"))
        self.gridLayout_3.addWidget(self.zAccelEdit, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_10)
        self.gridLayout_5.addWidget(self.groupBox_7, 2, 6, 1, 2)
        self.groupBox_12 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_12.setCheckable(False)
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sonarEdit = QtGui.QLineEdit(self.groupBox_12)
        self.sonarEdit.setStyleSheet(_fromUtf8("background-color: rgb(6, 5, 4);\n"
"color: rgb(64, 181, 64);\n"
"font: 9pt \"Monospace\";"))
        self.sonarEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.sonarEdit.setObjectName(_fromUtf8("sonarEdit"))
        self.horizontalLayout.addWidget(self.sonarEdit)
        self.gridLayout_5.addWidget(self.groupBox_12, 3, 6, 1, 1)
        self.groupBox_16 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cameraButton = QtGui.QPushButton(self.groupBox_16)
        self.cameraButton.setObjectName(_fromUtf8("cameraButton"))
        self.horizontalLayout_3.addWidget(self.cameraButton)
        self.gridLayout_5.addWidget(self.groupBox_16, 3, 7, 1, 1)
        self.abortButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.abortButton.setFont(font)
        self.abortButton.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.abortButton.setObjectName(_fromUtf8("abortButton"))
        self.gridLayout_5.addWidget(self.abortButton, 4, 6, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.motor0SpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor0Slider.setValue)
        QtCore.QObject.connect(self.motor0Slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor0SpinBox.setValue)
        QtCore.QObject.connect(self.motor1Slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor1SpinBox.setValue)
        QtCore.QObject.connect(self.motor1SpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor1Slider.setValue)
        QtCore.QObject.connect(self.motor2SpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor2Slider.setValue)
        QtCore.QObject.connect(self.motor2Slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor2SpinBox.setValue)
        QtCore.QObject.connect(self.motor3Slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor3SpinBox.setValue)
        QtCore.QObject.connect(self.motor3SpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor3Slider.setValue)
        QtCore.QObject.connect(self.masterMotorSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.masterMotorSpinBox.setValue)
        QtCore.QObject.connect(self.masterMotorSpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.masterMotorSlider.setValue)
        QtCore.QObject.connect(self.masterMotorSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor0Slider.setValue)
        QtCore.QObject.connect(self.masterMotorSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor1Slider.setValue)
        QtCore.QObject.connect(self.masterMotorSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor2Slider.setValue)
        QtCore.QObject.connect(self.masterMotorSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.motor3Slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_17.setTitle(_translate("MainWindow", "Motor A", None))
        self.groupBox_18.setTitle(_translate("MainWindow", "Motor B", None))
        self.groupBox_19.setTitle(_translate("MainWindow", "Motor C", None))
        self.groupBox_20.setTitle(_translate("MainWindow", "Motor D", None))
        self.groupBox_21.setTitle(_translate("MainWindow", "Master", None))
        self.groupBox_11.setTitle(_translate("MainWindow", "Connect", None))
        self.label_2.setText(_translate("MainWindow", "IP Address", None))
        self.ipAddressEdit.setText(_translate("MainWindow", "192.168.1.2", None))
        self.label_3.setText(_translate("MainWindow", "Port Number", None))
        self.portEdit.setText(_translate("MainWindow", "1337", None))
        self.connectButton.setText(_translate("MainWindow", "Connect", None))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Meower", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Meow1.wav", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "SurpriseMFcker.wav", None))
        self.pushButton_2.setText(_translate("MainWindow", "Launch", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Accelerometer", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "X-Axis", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "Y-Axis", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Z-Axis", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "Sonar", None))
        self.groupBox_16.setTitle(_translate("MainWindow", "Camera", None))
        self.cameraButton.setText(_translate("MainWindow", "Take Picture", None))
        self.abortButton.setText(_translate("MainWindow", "ABORT", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

