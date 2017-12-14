#!/usr/bin/python3

import curses
from curses import wrapper
from gpiozero import LED
from time import sleep


motor1F = LED(23) # pin 16 on rpi0
motor2F = LED(24) # pin 18
motor1R = LED(27) # pin 13
motor2R = LED(17) # pin 11

def Forward():
	motor1F.on()
	motor2R.on()
	sleep(0.1)
	motor1F.off()
	motor2R.off()
	sleep(0)

def Back():
	motor2F.on()
	motor1R.on()
	sleep(0.1)
	motor2F.off()
	motor1R.off()
	sleep(0)

def Clockwise():
	motor1F.on()
	motor1R.on()
	sleep(0.1)
	motor1F.off()
	motor1R.off()
	sleep(0)

def Anticlockwise():
	motor2F.on()
	motor2R.on()
	sleep(0.1)
	motor2F.off()
	motor2R.off()
	sleep(0)	


screen = curses.initscr()

curses.noecho()
curses.cbreak()

screen.keypad(True)

screen.addstr("Hello World!!!")
screen.addstr("PRESS THE ARROW KEYS TO MOVE THE CAR")
'''
def main(screen):
	screen.clear()

	for i in range (0, 11):
		v = i-10
		stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
		screen.refresh()
		screen.getkey()
wrapper(main)    

'''

while True:
	c = screen.getch()
	if c == curses.KEY_LEFT:
		screen.addstr(5,10, 'left key pressed')
		Anticlockwise()
		screen.refresh()
	elif c == curses.KEY_RIGHT:
		screen.addstr(5,50, 'right key pressed')
		Clockwise()
		screen.refresh()
	elif c == curses.KEY_UP:
		screen.addstr(2,30,'UP key pressed')
		Forward()
		screen.refresh()
	elif c == curses.KEY_DOWN:
		screen.addstr(9,30,'Down key pressed')
		Back()
		screen.refresh()


curses.nobreak()
screen.keypad(False) # Enable keypad Mode
curses.echo()
curses.endwin()











