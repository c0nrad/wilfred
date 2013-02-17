# accel.py
# Author: Daryl Bennet (DWB)
#
#   Retrieves information from the accelerometer

import sys,time

import Rpi.GPIO as GPIO

class Accelerometer:
    def __init__(self, pins):
        print "[*] Starting Acc:", pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pins, GPIO.IN)
        self.mPins=pins    
        
        #How often acc state is fetched in sec
        self.refresh_rate = 1
        self.moment_refresh= .005
        

    # getState
    #
    #    Gets the current state of the accerometer
    # in tuple form of (x, y, z) where x y z are values
    # in degrees specifying the offset from a flat state.

    # x: The degree of the nose, pointing up and down.
    #    If the nose is flat and level, the degree is zero
    #    If the nose is up at a 45, then the degree is 45
    #    If the nose is down, then -45
    #
    # y: From a birds eye perspective, this is the degree off
    #    the right wing. If it's flat with the round, the angle
    #    is 0.
    #    If wilfred is doing a barrel role, this value will change
    #    Same as the x value,
    #
    # z: Not implemented
    
    
    #Need spec sheet from acc to assign a non arbitrary number
    def getState(self):
        while True:
                
                #print '[+] Grabing first set of values'
                x1 = GPIO.input(self.mPins(1))
                y1 = GPIO.input(self.mPins(2))
                z1 = GPIO.input(self.mPins(3))
                
                time.sleep(self.moment_refresh)
                
                #print '[+] Grabing second set of values'
                x2 = GPIO.input(self.mPins(1))
                y2 = GPIO.input(self.mPins(2))
                z2 = GPIO.input(self.mPins(3))
                
                
                
                time.sleep(self.refresh_rate)
                
                x=x1-x2
                y=y1-y2
                z=z1-z2
                 
        return (x, y, z)
