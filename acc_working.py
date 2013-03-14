#Script for reading change in acc
#Daryl W. Bennett --kd8bny@gmail.com

#!/usr/bin/env python
import time
import os
import logging
import RPi.GPIO as GPIO

if __name__ == "__main__":      
	logging.basicConfig(filename='dX.log',level=logging.DEBUG)
	logging.info('Start Log:')

	GPIO.setmode(GPIO.BCM)

	# set up the SPI interface pins
	GPIO.setup(SPIMOSI, GPIO.OUT)	#Master output
	GPIO.setup(SPIMISO, GPIO.IN)		#Master input
	GPIO.setup(SPICLK, GPIO.OUT)		#Clk
	GPIO.setup(SPICS, GPIO.OUT)		#??channels
	GPIO.setup(accslp,GPIO.OUT)		#accslp --gains to read acc values

	
	always = 1

	# change these as desired - they're the pins connected from the
	# SPI port on the ADC to the Cobbler
	SPICLK = 18
	SPIMISO = 23
	SPIMOSI = 24
	SPICS = 25
	accslp=11

	GPIO.output(accslp,True) 			# set acc sleep high

	#axis setup
	vref =3.3				#voltage ref
	vzero=2.2				#0 volt ref
	Sensitivity = 1.5		# Selectable Sensitivity (1.5g,  or 6g)
	

	# Get values
	x = getX(vref, vzero, Sensitivity, always)

	# hang out and do nothing for a half second
        time.sleep(0.5)


# readadc code repect goes to adafruit
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


def getX(vref, vzero, Sensitivity, always):
	# set inintal values
	x = 0

	 # this keeps track of the last value
	lastX= 0      

	tolerance = 2       # to keep from being jittery we'll only change


	while True:

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
			x = (dX_value * vref / 1023 - vzero) / Sensitivity	#ouput in volts
			logging.info('X read in volts:',x)
	        # save the potentiometer reading for the next loop
	        lastX = dX_value
	return x        
