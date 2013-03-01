import socket
from debug import *

class Communication
    def __init__(self):
        self.HOST = ''
        self.PORT = 1337
        self.setupSocket()

    def setupSocket(self):
        infoMessage("communication::setupSocket: setting up socket on port: ", self.PORT)
        
        
        try:
            self.mSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.mSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.mSock.bind((self.HOST, self.PORT))
            self.mSock.listen(1)  
        except socket.error, socketError:
            if self.mSock:
                self,mSock.close()
                errorMessage("Could not open socket on \host: ", self.mHost, " port: ",
                             self.mPort, " reason: ", socketError)
                self.mSock = False
                return
        goodMessage("communication::setupSocket: connected to wilfred!")

    def checkConnection(self):
        if not self.mConn:
            return False
        return True
        
    def waitForClient(self):
        infoMessage("communication::waitForClient: waiting for client...")
        self.mConn, addr = self.mSock.accept()
        goodMessage("communication::waitForClient: client connected from: ", addr)
        
    def closeConnection(self):
        warningMessage("communication::closeConnect: closing connection...")

        if self.checkConnection():
            self.mConn.close()
            self.mSock = False
            self.mConn = False
        
    def getCommand(self):
        if not self.checkConnection():
            errorMessage("communication::getMessage: no connection established")
            return

        inData = self.mConn.recv(2048).strip()
        goodMessage("communication::getCommunication: recieved communication: \"", inData, "\"")
        return inData

    def sendMessage(self, data):
        if not self.checkConnection(): 
            errorMessage("communication::sendCommand: no connection established")
            return 

        goodMessage("communication::sendMessage: sending message: ", data.strip())
        self.mConn.sendall(data)



        
