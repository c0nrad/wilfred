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

import command
import driver
from debug import *

def mainLoop():
    wilfredCommand = command.Command()
    wilfredCommand.waitForClient()

    wilfredDriver = driver.Driver()

    while True:
        if not wilfredCommand.checkConnection():
            wilfredCommand.waitForClient()
        commands = wilfredCommand.getCommand()
        

        for commandData in commands.split('\n'):
            cmd = commandData.split(' ')[0].strip()
            if cmd == "": continue
            args = [arg.strip() for arg in commandData.split(' ')[1:]]
        
        
            # setMotorSpeed (0-3) (0-100)
            if cmd == "setMotorSpeed":
                motorNum = int(args[0])
                motorSpeed = int(args[1])
                wilfredDriver.setMotorSpeed(motorNum, motorSpeed)
            elif cmd == "playMeow":
                goodMessage("wilfred: playing meow from file: ", args[0])
                wilfredDriver.playMeow(args[0])
            elif cmd == "getAccel":
                goodMessage("wilfred: returning acceleration...")
                wilfredCommand.sendMessage("(0, 0, 0)")
            else:
                errorMessage("wilfred: command not recognized: ", cmd, ": ", args)
        

if __name__ == "__main__":
    mainLoop()
