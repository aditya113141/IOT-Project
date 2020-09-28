import paho.mqtt.client as mqttclient
import time

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("Client is connected")
        global connected
        connected = True
    else:
        print("Client is not connected")
def on_message(client,userdata,message):
    print("Message Recieved "+ str(message.payload.decode("utf-8")))
    print("Topic "+str(message.topic()))

connected = False
Messagerecieved = False

broker_address = "broker.mqttdashboard.com"
user = "."
password = "aditya113141"
client = mqttclient.Client("MQTT")
port = 1883
client.username_pw_set(user,password=password)
client.on_connect=on_connect
client.connect(broker_address,port)
client.loop_start()

top = "testy_adi"
client.subscribe(top)
while connected!=True:
    time.sleep(0.2)
while Messagerecieved!=True:
    time.sleep(0.2)
client.loop_stop()