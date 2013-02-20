import socket
import sys
import communication
from debug import *

class Command:
    def __init__(self, comm):
        self.mComm = comm
        
    def setMotorSpeed(self, motorNum, speed):
        infoMessage("command::setMotorSpeed: motorNum: ", motorNum, " motorSpeed: ", speed)

        try:
            motorNum = str(motorNum).strip()
            speed = str(speed).strip()
        except ValueError:
            errorMessage("command::setMotorSpeed: cannot convert \"", speed, "\" to string")
            return        
        
        payload = "setMotorSpeed " + str(motorNum).strip() + " " + str(speed).strip() + "\n"
        self.mComm.sendCommand(payload)

    def playMeow(self, fileName):
        infoMessage("command::playMeow: fileName: ", fileName)
        payload = "playMeow " + str(motorNum)
