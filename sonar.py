#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle

while True:
  time.sleep(0.1)

# Send 10us pulse to trigger
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  # Calculate pulse length
  elapsed = stop-start
  
  # Distance pulse travelled in that time is time
  # multiplied by the speed of sound (cm/s)
  distance = elapsed * 34000

  # That was the distance there and back so halve the value
  distance = distance / 2

  print "Distance : %.1f" % distance

# Reset GPIO settings
GPIO.cleanup()
