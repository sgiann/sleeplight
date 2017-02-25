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

#it is the scripts dudty to manage the lights.
#you will achieve that by sleeping.


###TODO: Use debugging funcitons to see how can you log all activity in a file. 


print "Start \'sleeplight \' job"
#Orange - still -> 20+10
print "Orange(18) - On :",datetime.datetime.now.time()
#create the still thread
orangeStill = LEDThreadStill("Orange",18,20)
#start the still thread fr orange light
LEDThreadStill.start()
#GPIO.output(18, GPIO.HIGH) -> hardcoded testng line.


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
print "End of sleeplight job"