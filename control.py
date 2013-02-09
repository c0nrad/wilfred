# control.py
# Author: Stuart Larsen (SCL)
#
#    Give it commands to move wilfred around, or to stabalize and such
#

class Control:
    def __init__(self):
        print "[*] Initializing Control module"
        self.mTLMotor = ""
        self.mTRMotor = ""
        self.mBLMotor = ""
        self.mBRMotor = ""

    def stabalize(self, craftAngles):
        print "[*] Stablizing craft"
        
        # Amount of thrust to keep the craft stabalized by itself
        normThrust = 35
        
        # Coefficent of motor thrust per degree of angle offset
        motorThrustK = .5

        print "[+] Current x-angle:", craftAngles[0], "target: 0"
        print "[+] Current y-angle:", craftAngles[1], "target: 0"

        # I have no idea how to stabalize from here
        
        self.mPrevCommand = "STABALIZE" 


if __name__ == "__main__":

    # Test code
    control = Control()
    control.stabalize((15, 15, 15))
