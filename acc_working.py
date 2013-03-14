#!/usr/bin/env python
import time
import os
import logging
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
always = 1
logging.basicConfig(filename='dX.log',level=logging.DEBUG)
logging.info('Start Log:')


# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7) --KEEP
def readad(adcnum, clockpin, mosipin, misopin, cspin):     
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
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

def accSlp(in_value,out_value):
	while in_value:
		time.sleep(0.05)
		value  = True
		time.sleep(0.05)
		value = False
	return value

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
slp=11

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(slp,GPIO.OUT)

#axis setup
x = 0;

lastX = 0       # this keeps track of the last potentiometer value
tolerance = 2       # to keep from being jittery we'll only change
                    # volume when the pot has moved more than 5 'counts'




while True:

	wantsleep=True
	#sleep count for acc
	slp = accSlp(wantsleep,accClk)

        # delta X
        dX = False

        # read the analog pin
        dX_value = readadc(x, SPICLK, SPIMOSI, SPIMISO, SPICS)
        # how much has it changed since the last read?
        adjX = abs(dX_value - lastX)

        if always:
                print "dX:", dX_value
                print "adjX:", adjX
                print "lastX", lastX

        if ( adjX > tolerance ):
               dX = True

        if always:
                print "dX changed", dX

        if ( dX ):
                logging.info('dX:',dX_value)
        # save the potentiometer reading for the next loop
        lastX = dX_value
        # hang out and do nothing for a half second
        time.sleep(0.5)
