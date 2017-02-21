#iport libs
import RPi.GPIO as GPIO
import time
import datetime

#import my fns
from fn_flash_led import flash_led

#Control led lights based on day and time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin_number, GPIO.OUT)

#this will be called by the chrontab job
#once, at the time needed.

#it is the sscripts dudty to manage the lights.
#you will achieve that by sleeping.

#Orange - still -> 20+10
#print "Orange(18) - On :",datetime.datetime.now.time()
#GPIO.output(18, GPIO.HIGH)


#Orange - still & Green - blink -> 10
#print "Green(x) - Blink :",datetime.datetime.now.time()
#flash_led(x,1)

#Green - still -> 5
#log time

#Green - still & Red - blink ->5
#log time

#Red still -> 5
#log time

#Red - blink -> 5
#log time
