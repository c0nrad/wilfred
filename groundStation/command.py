import socket
from debug import *

class Command:
    def __init__(self):
        self.HOST = '192.168.1.3'
        self.PORT = 1337
        self.setupSocket()

    def setupSocket(self):
        infoMessage("command::setupSocket: setting up socket on port: ", self.PORT)        
        self.mSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mSock.connect((self.HOST, self.PORT))
        self.mConn = self.mSock 
        
    def closeConnection(self):
        warningMessage("command::closeConnect: closing connection...")
        self.mConn.close()
        
    def getMessage(self):
        inData = self.mConn.recv(2048).strip()
        goodMessage("command::getCommand: recieved command: \"", inData, "\"")
        return inData

    def sendCommand(self, data):
        goodMessage("command::sendMessage: sending message", data)
        self.mConn.sendall(data)
        
    def setMotorSpeed(self, motorNum, speed):
        infoMessage("command::setMotorSpeed: motorNum: ", motorNum, " motorSpeed: ", speed)
        
        payload = "setMotorSpeed " + str(motorNum).strip() + " " + str(speed).strip() + "\n"
        self.sendCommand(payload)
