import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# The input pin of the Sensor will be declared. Additional to that the pullup resistor will be activated
tiltpin = 27
ledpin = 17
GPIO.setup(tiltpin, GPIO.IN)
GPIO.setup(ledpin,GPIO.OUT)

print ("Sensor-test [press ctrl+c to end]")

# This output function will be started at signal detection
def outFunction(null):
    print("Signal detected")
    GPIO.output(ledpin,1)

# The output function will be activated after a signal was detected ( falling signal edge ).
GPIO.add_event_detect(tiltpin, GPIO.FALLING, callback=outFunction, bouncetime=100) 

# main program loop 
try:
    while True:
        time.sleep(1)

# Scavenging work after the end of the program
except KeyboardInterrupt:
    GPIO.cleanup()