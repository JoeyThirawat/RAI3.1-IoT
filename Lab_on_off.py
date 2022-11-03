import paho.mqtt.client as paho
broker = "iotkmitl.ddns.net"
port = 9001

import RPi.GPIO as GPIO
import time

LED_OUT = 26
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_OUT, GPIO.OUT)
GPIO.output(LED_OUT, False)


def on_message(mosq,obj,msg):
    global message
    print(msg.payload.decode("utf-8"))
    message = msg.payload.decode("utf-8")
    if (message == "on"):
        GPIO.output(LED_OUT, True)
    else:
        GPIO.output(LED_OUT, False)

def on_subscribe(mosq,obj,mid,granted_qos):
    print("Subscribed:"+str(mid)+" "+str(granted_qos))

def on_publish(mosq,obj,mid,granted_qos):
    print("data published \n")
    pass

client1 = paho.Client("control3",transport="websockets")
client1.username_pw_set(username="kmitlcie",password = "ciehasmoney")
client1.on_publish = on_publish
client1.on_subscribe = on_subscribe
client1.on_message = on_message

client1.connect(broker,port)
#ret = client1.publish("Joey","on")

client1.subscribe("Joey",0)
client1.loop_forever()