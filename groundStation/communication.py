import socket
import sys
from debug import *

class Communication:
    def __init__(self):
        self.mHost = '192.168.1.2'
        self.mPort = 1337
        self.TIMEOUT = 3
        self.setupSocket(self.mHost, self.mPort)
        self.mSock = False
        self.mConn = False

    def setupSocket(self, host, port):
        self.mHost = host
        self.mPort = port
        infoMessage("communication::setupSocket: setting up socket on host: ", 
                    self.mHost, " port: ", self.mPort)                

        try:
            self.mSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.mSock.settimeout(self.TIMEOUT)
            self.mSock.connect((self.mHost, self.mPort))
            self.mConn = self.mSock 
        except socket.error, socketError:
            if self.mSock:
                self.mSock.close()
                errorMessage("Could not open socket on \host: ", self.mHost, " port: ",
                             self.mPort, " reason: ", socketError)
                return
        goodMessage("communication::setupSocket: connected to wilfred!")
        
    def checkConnection(self):
        if not self.mSock or not self.mComm or self.mSock == "" or self.mComm == "":
            return False
        else:
            return True

    def closeConnection(self):
        warningMessage("communication::closeConnect: closing connection...")

        if self.checkConnection():
            self.mConn.close()
        
    def getMessage(self):
        if not self.checkConnection():
            errorMessage("communication::getMessage: no connection established")
            return

        inData = self.mConn.recv(2048).strip()
        goodMessage("communication::getCommunication: recieved communication: \"", inData, "\"")
        return inData

    def sendCommand(self, data):
        if not self.checkConnection(): 
            errorMessage("communication::sendCommand: no connection established")
            return 

        goodMessage("communication::sendMessage: sending message", data)
        self.mConn.sendall(data)
        

    
