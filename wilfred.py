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


class Wilfred:
    def __init__(self):
        print "[*] Wilfred is booting up..."
    
        # Start components

    def mainLoop(self):
        while True:
            # Gather Command

            # Gather recon

            # Drive the controllers

if __name__ == "__main__":
    wilfred = Wilfred()
    wilfred.mainLoop();

    
