import threading
import time

#param list
#name : Give as name the colour of the LED to be handled.
#pin_number - The pin number that the LED is hooked at.
#dtime_mins - Give the desired time in minutes that you want the led to blink for.

class LEDThreadStill(threading.Thread):
    def __init__(self, name, pin_number, dtime_mins)
        threading.Thread._init__(self)
        self.name = name
        self.pin_number = pin_number
        self.dtime_mins = dtime_mins

#the main funciton f this class
#will blink the LED on for dtime mins.
    def run(self):
        print "Thread start. Name:", self.name, " - blink. time:" ,datetime.datetime.now.time()

        #blink
        while true
            
            if time.time()>timeout:
                break
        #end of while
            
        print "Thread end. Name:", self.name, " time:" ,datetime.datetime.now.time()
