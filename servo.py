import RPi.GPIO as GPIO
import time

class Servo(object):
    def __init__(self,port):
        self.port = port
	GPIO.setmode(GPIO.BOARD)			
   	GPIO.setup(self.port, GPIO.OUT)

    def move1(self):
        GPIO.setmode(GPIO.BOARD)			
   	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(18, GPIO.LOW)
	p = GPIO.PWM(12,50)
	p.start(7)
	try:
            GPIO.setmode(GPIO.BOARD)			
   	    GPIO.setup(12, GPIO.OUT)
	    p.ChangeDutyCycle(7)
	    time.sleep(1)
	    p.ChangeDutyCycle(13)
            ## time.sleep(5)
	    ## p.ChangeDutyCycle(7.5)
	except KeyboardInterrupt:
	    p.stop()
	    GPIO.cleanup()
    def move2(self):
        GPIO.setmode(GPIO.BOARD)			
   	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(16,GPIO.LOW)
	GPIO.output(18,GPIO.HIGH)
        p = GPIO.PWM(12,50)
	p.start(13)
	try: 
	    p.ChangeDutyCycle(13)
	    time.sleep(1)
	    p.ChangeDutyCycle(7)
            ## time.sleep(5)
	    ## p.ChangeDutyCycle(7.5)
	except KeyboardInterrupt:
	    p.stop()
	    GPIO.cleanup()

