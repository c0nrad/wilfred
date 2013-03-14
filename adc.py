#!/usr/bin/env python
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
DEBUG = 1

class ADC():
    SPICLK = 18     # CLOCK
    SPIMISO = 23    # Master In Slave Out 
    SPIMOSI = 24    # Master Out Slave In
    SPICS = 25      # Chip Selecte

    def __init__(self):
        # set up the SPI interface pins
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    def readadc(self, adcnum):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1

        clockpin = self.SPICLK
        mosipin = self.SPIMOSI
        misopin = self.SPIMISO
        cspin = self.SPICS
        
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80): # See if the last bit is high
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

# ADC pin for X, Y, Z
accel_adc = [0, 1, 2]
accel_axis = ["X", "Y", "Z"]

if __name__ == "__main__":
    adc1 = ADC()

    millivolts = 3300 / 1024
    mv_per_g = 800
    
    while True:
        accel_mv = [millivolts * adc1.read(adcPin) for adcPin in accel_adc]
        accel_g = [mv / mv_per_g for mv in accel_mv]

        for x in range(len(accel_axis)):
            axis = accel_axis[x]
            print "[",axis,"] Millivolts:", accel_mv[x], "\t g:", accel_g[x]
            
    time.sleep(.5)