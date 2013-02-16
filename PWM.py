# PWM.py
# Authors: 
#     Stuart C. Larsen (SCL), Daryl W. Bennet (DWB)
#
# Description: 
#     Simple PWM implementation of digital pin Pulse Width Modulation. Creates a thread to quickly switch the pin from high to low.
#
# Usage:
#    motor1 = PWM(1)
#    motor1.setSpeed(50) # Run motor at 50% speed
#
# Interface:
#    PWM.PWM(pin):
#        Initialized the pin for output, and creates and startes the switching thread
#
#    PWM.setSpeed(value):
#        Set the speed of the PWM from 0-99 based on how fast you'd like the motor to go
import time
import sys

from threading import Thread, Lock
import RPi.GPIO as GPIO

class PWM:

    def __init__(self, pin):
        print "[*] Starting PWM on pin:", pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)    
        self.mPin = pin
        self.SWITCHING_FREQ = 50.

        self.mHighPercent = .5
        self.mHighPercentLock = Lock()


        print "[+] Starting the PWM Thread"
        self.mThread = Thread(target=self.runPWM)
        try:
            self.mThread.start()
        except (KeyboardInterrupt, SystemExit):
            sys.exit()
        return
                
    def runPWM(self):
        while True:
            highTime = self.calculateHighTime(self.SWITCHING_FREQ, self.getHighPercent()) 
            lowTime = self.calculateHighTime(self.SWITCHING_FREQ, 1 - self.getHighPercent())
        
            GPIO.output(self.mPin, GPIO.HIGH)
            #print "[+] High sleep time: ", highTime
            time.sleep(highTime)

            GPIO.output(self.mPin, GPIO.LOW)
            #print "[+] Low sleep time: ", lowTime
            time.sleep(lowTime)
    
    def calculateHighTime(self, switchFreq, highPercent):
        highTime = highPercent/switchFreq
        return highTime
        # beautiful  /sniff 
        
    def setSpeed(self, value):
        print "[+] Setting new speed:", value
        self.setHighPercent(value / 100.)
        
    def calculateLowTime(self, switch_freq, highPercent):
        return 1 - self.calculateHighTime(switch_freq, highPercent)
    
    def getHighPercent(self):
        self.mHighPercentLock.acquire() 
        temp = self.mHighPercent
        self.mHighPercentLock.release()
        return temp
    
    def setHighPercent(self, value):
        if value > 1 or value < 0:
            print "[-] PWM::setHighPercent must be between 0 and 1"
        self.mHighPercentLock.acquire()
        self.mHighPercent = value
        self.mHighPercentLock.release()
        
def test(motor1):
    print "[*] Begining motor test!"
    motor1 = PWM(7)
    
    print "[+] Stopping motor..."
    motor1.setSpeed(0)
    time.sleep(5)
    
    print "[+] Setting motor to 50% speed..."
    motor1.setSpeed(50)
    time.sleep(5)
    
    print "[+] Setting motor to 100% speed..."
    motor1.setSpeed(100)
    time.sleep(5)
    
    print "[+] Testing complete! Motor stoping..."
    motor1.setSpeed(0)
    

def fade(motor1):
    delay = .1
    speed = 0
    while True:
        speed = (speed + 1) % 20
        motor1.setSpeed(speed)
        time.sleep(delay)
    
if __name__ == "__main__":
    motor1 = PWM(7)

    fade(motor1)

