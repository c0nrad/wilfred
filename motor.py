# motor.py
# Author: Daryl Bennet (DWB)
#
#   Driver for motors

class Motor:
    def __init__(self, pin):
        print "[*] Initializing motor on pin:", pin
        # Set up pins
        self.mPin = pin

        pass

    # setSpeed
    #
    #    Accepts a speed value from -100 to 100, and
    # sets the motor speed according to those values,
    # with 0 being off, 100 being full forward, and -100
    # being full reverse.
    def setSpeed(self, speed):
        print "[*] Setting speed on motor:", self.mPin, "speed:", speed
        self.mCurrentSpeed = speed

        pass

if __name__ == "__main__":
    # Code for testing
    m1 = Motor(1)
    m1.setSpeed(75)
