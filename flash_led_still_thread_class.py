import threading
import time

#params
#name : Give as name the colur of the LED to be handled
#dtime_mins: Give the desired time in minutes that you want the led to stay On

class LEDThreadStill(threading.Thread):
    def __init__(self, name, pin_numbr, dtime_mins)
        threading.Thread._init__(self)
        self.name = name
        self.pin_number = pin_number
        self.dtime_mins = dtime_mins

#default function turns of the choosen led by seting
#to low the pin number that takes as argument
    def default(pin_number):
        GPIO.output(self.pin_number, GPIO.LOW)

    def run(self):
        print "Thread start. Name:", self.name, " time:" ,datetime.datetime.now.time()

        #turn LED off in case it is on.
        self.default(self.pin_number)

        timeout = time.time + (dtime_mins*60)
        
        #light still
        GPIO.output(pin_number, GPIO.HIGH)
        while true
            
            if time.time()>timeout:
                break
        #end of while
        
        self.default(self.pin_number)

        print "Thread end. Name:", self.name, " time:" ,datetime.datetime.now.time()
