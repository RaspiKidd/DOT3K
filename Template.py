#!/usr/bin/env python

"""
This is a program to fetch and display your IP address, Gateway address,
Host name and current date and time.
"""

# AUTHOR: Kerry Kidd		V: 		DATE: 

import signal
# Libraries for display

import dot3k.joystick as joystick
import dot3k.lcd as lcd
import dot3k.backlight as backlight

# Button
@joystick.on(joystick.BUTTON)
def handle_button(pin):
	print("You Pressed me")
	lcd.clear()
	backlight.rgb(255,0,0)
	lcd.write("You Pressed Me")

# Up 
@joystick.on(joystick.UP)
def handle_up(pin):
	print("This is Up")
	lcd.clear()
	backlight.rgb(0,255,0)
	lcd.write("This is up")

# Down
@joystick.on(joystick.DOWN)
def handle_down(pin):
	print ("this is down")
	lcd.clear()
	backlight.rgb(0,0,255)
	lcd.write("this is down")

# Left
@joystick.on(joystick.LEFT)
def handle_left(pin):
	print ("This is left")
	lcd.clear()
	backlight.rgb(0,255,255)
	lcd.write("This is left")
# Right
@joystick.on(joystick.RIGHT)
def handle_right(pin):
	print ("This is right")
	lcd.clear()
	backlight.rgb(255,255,255)
	lcd.write("This is right")

# Prevent the script from exiting
signal.pause()
