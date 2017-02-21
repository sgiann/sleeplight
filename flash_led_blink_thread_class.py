import threading
import time

class LEDThreadStill(threading.Thread):
    def __init__(self, name, pin_numbr, dtime_mins)
        threading.Thread._init__(self)
        self.name = name
        self.pin_number = pin_number
        self.dtime_mins = dtime_mins

    def run(self):
        print "Thread start. Name:", self.name, " time:" ,datetime.datetime.now.time()

        #blink
        while true
            
            if time.time()>timeout:
                break
        #end of while
            
        print "Thread end. Name:", self.name, " time:" ,datetime.datetime.now.time()
