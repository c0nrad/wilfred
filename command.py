import socket
from debug import *

class Command:
    def __init__(self):
        self.HOST = ''
        self.PORT = 1337
        self.setupSocket()

    def setupSocket(self):
        infoMessage("command::setupSocket: setting up socket on port: ", self.PORT)
        self.mSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mSock.bind((self.HOST, self.PORT))
        self.mSock.listen(1)    
        
    def waitForClient(self):
        infoMessage("command::waitForClient: waiting for client...")
        self.mConn, addr = self.mSock.accept()
        goodMessage("command::waitForClient: client connected from: ", addr)
        
    def closeConnection(self):
        warningMessage("command::closeConnect: closing connection...")
        self.mConn.close()
        
    def getCommand(self):
        inData = self.mConn.recv(2048).strip()
        goodMessage("command::getCommand: recieved command: \"", inData, "\"")
        return inData

    def sendMessage(self, data):
        goodMessage("command::sendMessage: sending message", data)
        self.mConn.sendall(data)
        
        
