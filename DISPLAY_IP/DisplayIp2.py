#!/usr/bin/env python

"""
This is a program to fetch and display your IP address, Gateway address,
Host name and current date and time.
"""

# AUTHOR: Kerry Kidd		V: 2		DATE: 23/02/15

# Libraries for display

import dot3k.joystick as joystick
import dot3k.lcd as lcd
import dot3k.backlight as backlight

# Libraries to get IP 
import signal
import socket
import os

# Library for time and date
import time

# The next block of code gets the IP address Host name and gateway address
gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((gw[2],0))
ipaddr = s.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()

# The next line prints the IP address, gateway address and host name
#print ("IP: ", ipaddr, "GW: ", gateway, "HOST: ", host)


# Displays the IP address when the joystick is pressed
@joystick.on(joystick.BUTTON)
def handle_button(pin):
	#print("IP: ", ipaddr)
	lcd.clear()
	backlight.rgb(255,0,0)
	lcd.write(ipaddr)

# Displays the Host when the joystick has been moved up
@joystick.on(joystick.UP)
def handle_up(pin):
	#print("HOST: ", host)
	lcd.clear()
	backlight.rgb(0,255,0)
	lcd.write(host)

# Displays "Nothing Assigned" when the joystick has been moved down
@joystick.on(joystick.DOWN)
def handle_down(pin):
	#print (time.strftime("%H:%M%S"))
	lcd.clear()
	backlight.rgb(0,0,255)
	lcd.write(time.strftime("%H:%M:%S"))

# Displays the gateway when the joystick has been moved left
@joystick.on(joystick.LEFT)
def handle_left(pin):
	#print ("GATEWAY: ", gateway)
	lcd.clear()
	backlight.rgb(0,255,255)
	lcd.write(gateway)

@joystick.on(joystick.RIGHT)
def handle_right(pin):
	#print (time.strftime("%d%m%y"))
	lcd.clear()
	backlight.rgb(255,255,255)
	lcd.write(time.strftime("%d/%m/%y"))

# Prevent the script from exiting
signal.pause()

