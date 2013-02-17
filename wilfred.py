# wilfred.py
# Authors
#   Stuart C. Larsen (SCL)
#   Daryl W. Bennet (DWB)

#   Set up three main modules (command, control, reconnaissance),
# and then enter main event loop.
#
# Command:
#   Gather mission priorities and objectives, such as turn left, turn right
# goto GPS 45, 65, land, take off.
#
# Control:
#   Fly the craft to complete the command objective.
#
# Reconnaissance:
#   Gather information about wilfreds current position.
#
# Main Event Loop:
#   Check command listing for new updates, check reconnaisannce for current
# posistion, and then control the craft to the correct zone. Main loop will
# be a very fast feedback loop.

from PyQt4.QtGui import *
from PyQt4 import *
from mainWindow import *
import sys


if __name__ == "__main__":
    

    app = QtGui.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.setupUi()
    app.exec_loop()

    
