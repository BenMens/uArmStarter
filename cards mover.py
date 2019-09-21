# uArm Swift Pro - Python Library Example
# Created by: Richard Garsthagen - the.anykey@gmail.com
# V0.3 - June 2018 - Still under development
#
# Use Python 2.x!

from uarm import uArmRobot
import time


#Configure Serial Port
serialport = "/dev/ttyACM0"  # for linux like system

# Connect to uArm 
myRobot = uArmRobot.robot(serialport, 1)   # user 0 for firmware < v4 and use 1 for firmware v4
myRobot.debug = True  # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal

wait = 0
speed = 12000
numCarts = 7

time.sleep(1)

myRobot.goto(  200, 0, 100, 600)

time.sleep(5)

for i in range(0, numCarts):

    time.sleep(wait)

    myRobot.goto(  200, 0, 15 - i, speed)

    time.sleep(wait)

    myRobot.goto(  200, 0, (numCarts - i) * 0.5 + 1, speed)

    time.sleep(wait)

    myRobot.pump(True)

    time.sleep(1)

    myRobot.goto(  200, 0, 100, speed)

    time.sleep(wait)


    myRobot.goto(  200, 180, 100, speed)

    time.sleep(wait)

    myRobot.goto(  200, 180, 6 + i, speed)

    time.sleep(wait)

    myRobot.pump(False)

    time.sleep(1)


myRobot.goto(  200, 0, 100, speed)

time.sleep(1)


#Disconnect serial connection
myRobot.disconnect()
