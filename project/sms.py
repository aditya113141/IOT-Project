import requests
import json



def send_sms(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    params ={
            'authorization':'API',
            'sender_id':'FSTSMS',
            'message':message,
            'route':'p',
            'numbers':number,
            'language':'english',
        }
    
    response = requests.get(url,params=params)
    dic = response.json()
    
#send_sms("9662106867","This is Aditya")
