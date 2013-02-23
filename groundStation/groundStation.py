import resources_rc
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from communication import Communication
from command import Command
import mainWindow
import sys

from debug import *

class GroundStation(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.wilfredCommunication = Communication()
        self.wilfredCommand = Command(self.wilfredCommunication)

        # Motor Sliders
        self.connect(self.motor0SpinBox, SIGNAL("valueChanged(int)"), self.updateMotor0)
        self.connect(self.motor1SpinBox, SIGNAL("valueChanged(int)"), self.updateMotor1)
        self.connect(self.motor2SpinBox, SIGNAL("valueChanged(int)"), self.updateMotor2)
        self.connect(self.motor3SpinBox, SIGNAL("valueChanged(int)"), self.updateMotor3)
        
        # Connect
        self.connect(self.connectButton, SIGNAL("pressed()"), self.connectToWilfred)
        self.connect(self.disconnectButton, SIGNAL("pressed()"), self.disconnectFromWilfred)
        
        # Accelerometer
        self.initAccelerometers()

        # Abort Button
        self.connect(self.abortButton, SIGNAL("pressed()"), self.abortWilfred)

    def updateMotor0(self, value):
        goodMessage("updateMotor0: new motor value: ", value)
        self.wilfredCommand.setMotorSpeed(0, value)

    def updateMotor1(self, value):
        goodMessage("updateMotor1: new motor value: ", value)
        self.wilfredCommand.setMotorSpeed(1, value)

    def updateMotor2(self, value):
        goodMessage("updateMotor2: new motor value: ", value)
        self.wilfredCommand.setMotorSpeed(2, value)

    def updateMotor3(self, value):
        goodMessage("updateMotor3: new motor value: ", value)
        self.wilfredCommand.setMotorSpeed(3, value)
        
    def connectToWilfred(self):
        ip = str(self.ipAddressEdit.text()).strip()
        port = int(self.portEdit.text())
        self.wilfredCommunication.setupSocket(ip, port)
        
    def disconnectFromWilfred(self):
        self.wilfredCommunication.closeConnection()

    def initAccelerometers(self):
        timer = QTimer(self);
        self.connect(timer, SIGNAL("timeout()"), self.updateAccelerometer)
        self._counter = 0
        timer.start(1000);

    def updateAccelerometer(self):
        if not self.wilfredCommunication.checkConnection():
            return

        (xAccel, yAccel, zAccel) = self.wilfredCommand.getAccel()
        self.xAccelEdit.setText(str(xAccel))
        self.yAccelEdit.setText(str(yAccel))
        self.zAccelEdit.setText(str(zAccel))

    def abortWilfred(self):
        self.masterMotorSlider.setValue(0)
        errorMessage("Aborting wilfred")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))

    gs = GroundStation()
    gs.show()
    
    sys.exit(app.exec_())
