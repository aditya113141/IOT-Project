import RPi.GPIO as GPIO
import time
from sms import *
import os
GPIO.setmode(GPIO.BCM)
 
TRIG =23
ECHO =24
pulse_start = 0
pulse_end = 0
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
     
     
     
     while(True):
         GPIO.output(TRIG, False)
         print ("Waiting for Sensor to settle")
         time.sleep(2);
         
         GPIO.output(TRIG,True)
         time.sleep(0.00001)
         GPIO.output(TRIG,False)
         
         while GPIO.input(ECHO)==0:
             pulse_start = time.time()
         while GPIO.input(ECHO)==1:
             pulse_end = time.time()
         pulse_duration = pulse_end - pulse_start
         distance = round(pulse_duration *17150,2)
         
         print(distance)
         time.sleep(2)
         
         if(distance < 180):
             
             os.system("python3 entryinterface2.py")
             exit()
         
except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup()
         
         