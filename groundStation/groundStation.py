import resources_rc
from PyQt4 import QtCore, QtGui
import mainWindow
import sys

class GroundStation(QtGui.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))

    gs = GroundStation()
    gs.show()
    
    sys.exit(app.exec_())
