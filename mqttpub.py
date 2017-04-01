# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:29:53 2017

@author: k
"""
import paho.mqtt.publish as publish

publish.single("paho/zgur/singlein", "ozgurdata", hostname="iot.eclipse.org")