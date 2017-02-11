#
#
#
#

def flash_led(pin_number, dtime)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin_number, GPIO.OUT)
    
    print "fn: flash_led -- LED On"
    GPIO.output(pin_number, GPIO.HIGH)
    time.sleep(dtime)
    
    print "fn: flash_led -- LED Off"
    GPIO.output(pin_number, GPIO.LOW)
    return;
        
#test the function above
#flash_led(18,1)
#time.sleep(1)
#flash_led(18,2)