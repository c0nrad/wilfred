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
import wiringpi

from threading import Thread, Lock
import RPi.GPIO as GPIO

class PWM:
    self.SWITCHING_FREQ = 100 

    def __init__(self, pin):
        print "[*] Starting PWM on pin:", pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)    
        self.mPin = pin
        
        print "[+] Starting the PWM Thread"
        self.mThread = Thread(target=self.runPWM)
        self.mThread.start()
        
        self.mHighPercent = .5
        self.mHighPercentLock = Lock()
                
     def runPWM(self):
        while True:
            highTime = calculateHighTime(self.SWITCHING_FREQ, self.getHighPercent()) # <---
            lowTime = calculateHighTime(self.SWITCHING_FREQ, 1 - self.getHighPercent())
        
            GPIO.digitalWrite(self.mPin, GPIO.HIGH)
            sleep(highTime)
            
            GPIO.digitalWrite(self.mPin, GPIO.LOW)
            sleep(lowTime)
    
    def calculateHighTime(self, switchFreq, highPercent):
        highTime = highPercent/switchFreq
        return highTime
        # beautiful  /sniff 
        
    def setSpeed(self, value):
        print "[+] Setting new speed:", value
        self.setHighPercent(value / 100)
        
    def calculateLowTime(self, switch_freq, highPercent):
        return 1 - self.calculateHighTime(switch_freq, highPercent)
    
    def getHighPercent(self):
        self.mHighPercentLock.acquire() 
        temp = self.mHighPercent
        self.mHighPercentLock.release()
        return temp
        
    def setHighPercent(self, value)
        if value > 1 or value < 0:
            print "[-] PWM::setHighPercent must be between 0 and 1"
        self.mHighPercentLock.acquire()
        self.mHighPercent = value
        self.mHighPercentLock.release()
        
def test():
    print "[*] Begining motor test!"
    motor1 = PWM(1)
    
    print "[+] Stopping motor..."
    motor1.setSpeed(0)
    thread.sleep(2)
    
    print "[+] Setting motor to 50% speed..."
    motor1.setSpeed(50)
    thread.sleep(2)
    
    print "[+] Setting motor to 100% speed..."
    motor1.setSpeed(100)
    thread.sleep(2)
    
    print "[+] Testing complete! Motor stoping..."
    motor1.setSpeed(0)
    
if __name__ == "__main__":
    test()
