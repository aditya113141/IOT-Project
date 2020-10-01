import requests
import json

from tkinter import *
from tkinter.messagebox import *

def send_sms(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    params ={
            'authorization':'Fp51aCSfi9TzWeZJt4jvnyMdRVGHobNrwEDLmsqc2xIPk0uQU3m8AOE9N7WygYVpcovF3iSf1xqtZdHk',
            'sender_id':'FSTSMS',
            'message':message,
            'route':'p',
            'numbers':number,
            'language':'english',
        }
    
    response = requests.get(url,params=params)
    dic = response.json()
    print(dic)
#send_sms("9662106867","This is Aditya")