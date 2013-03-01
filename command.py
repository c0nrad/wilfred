import socket
from debug import *

class Command:
    def __init__(self, comm):
        self.mComm = comm

        self.MOTOR_PIN_0 = 3
        self.MOTOR_PIN_1 = 5
        self.MOTOR_PIN_2 = 7
        self.MOTOR_PIN_3 = 11

        self.mMotor0 = PWM.PWM(self.MOTOR_PIN_0)
        self.mMotor1 = PWM.PWM(self.MOTOR_PIN_1)
        self.mMotor2 = PWM.PWM(self.MOTOR_PIN_2)
        self.mMotor3 = PWM.PWM(self.MOTOR_PIN_3)
        
    def setMotorSpeed(self, motorNum, speed):
        goodMessage("command::setMotorSpeed: motorNum: ", motorNum, " speed: ", speed)

        if motorNum > 3 or motorNum < 0:
            errorMessage("command::setMotorSpeed: ", motorNum, " is not a value motor number")

        if motorNum == 0:
            self.mMotor0.setSpeed(speed)
        elif motorNum == 1:
            self.mMotor1.setSpeed(speed)
        elif motorNum == 2:
            self.mMotor2.setSpeed(speed)
        elif motorNum == 3:
            self.mMotor3.setSpeed(speed)
        else:
            errorMessage("command::setMotorSpeed: ", motorNum, " is not a value motor number")
        

    def playMeow(self, fileName):
        goodMessage("command::playMeow: playing meow from file: ", fileName)
        warningMessage("playMeow not implemented")
        

    def getAccel(self):
        infoMessage("command::getAccel returning the current accelerometer readings")
        payload = "(0, 0, 0)\n"
        self.mComm.sendMessage(payload)

        
