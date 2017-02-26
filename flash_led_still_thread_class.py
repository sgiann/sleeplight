import threading
import datetime

#param list
#name - Give as name the colour of the LED to be handled.
#pin_number - The pin number that the LED is hooked at.
#dtime_mins - Give the desired time in minutes that you want the led to stay On.

class LEDThreadStill(threading.Thread):
    def __init__(self, name, pin_number, dtime_mins):
        threading.Thread.__init__(self)
        self.name = name
        self.pin_number = pin_number
        self.dtime_mins = dtime_mins

#the main funciton f this class
#will turn the LED on for dtime mins.
    def run(self):
        print "Thread start. Name:", self.name, " - still. time:" ,datetime.datetime.now()

        #turn LED off in case it is on.
        self.default(self.pin_number)

        timeout = time.time + (dtime_mins*60)
        
        #light still
        GPIO.output(self.pin_number, GPIO.HIGH)
        self.default(self.pin_number)

        print "Thread end. Name:", self.name, " time:" ,datetime.datetime.now()

#default function turns of the choosen led by setting
#to low the pin number that takes as argument
    def default(pin_number):
        GPIO.output(self.pin_number, GPIO.LOW)
