# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:32:18 2017

@author: k
"""
import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("paho/zgur/single")

def on_message(client, userdata, msg):
    print str(msg.payload)
    print msg.topic

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
