import RPi.GPIO as GPIO
import time
import os
from sms import *
import psutil
pin = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pin,GPIO.OUT)
#os.system('python3 entryinterface.py')
cnt = 0
GPIO.output(pin,0)


numb=[]
def MemberList(filename):

   
    with open(filename) as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.split(',')
        numb.append(line[2])


def fun(ev=None):
    global cnt
    cnt = cnt+15
    if(cnt>0):
        print("detected")
        msg = "Alert! Someone is trying to open the door."
        program1 = "entryinterface2.py"
        program2 = "main.py"
        program3 = "test_ultrasound.py"
        for it in numb:
            #send_sms(it,msg)
            pass
        for proc in psutil.process_iter():
            if proc.name()==program1 :
                proc.kill()
            elif proc.name()==program2:
                proc.kill()
            elif proc.name()==program3:
                proc.kill()
        while True:
            GPIO.output(pin,1)
            
MemberList('member.txt')
try:
    while True:
         if not 'event' in locals():
            event=GPIO.add_event_detect(4, GPIO.FALLING, callback = fun,bouncetime=200)
except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.output(pin,0)
    GPIO.cleanup()
