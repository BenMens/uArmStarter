# uArm Swift Pro - Python Library Example
# Created by: Richard Garsthagen - the.anykey@gmail.com
# V0.3 - June 2018 - Still under development
#
# Use Python 2.x!

from uarm import uArmRobot
import time


#Configure Serial Port
# serialport = "/dev/ttyACM0"  # for linux like system
serialport = "/dev/tty.usbmodem14101"

# Connect to uArm 
myRobot = uArmRobot.robot(serialport, 1)   # user 0 for firmware < v4 and use 1 for firmware v4
myRobot.debug = True  # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal

wait = 1
speed = 200
numCarts = 8
cardThickness = 4

pos1 = [200, 0, 5]

pos2 = [200, 180, 5]

time.sleep(1)

myRobot.goto(  200, 0, 100, 10)

time.sleep(5)


for i in range(0, numCarts):

    time.sleep(wait)

    myRobot.goto(  pos1[0], pos1[1], pos1[2] + 100, speed)

    time.sleep(wait)

    myRobot.goto(  pos1[0], pos1[1], pos1[2] + (numCarts - i) * cardThickness, speed)

    myRobot.pump(True)

    time.sleep(2)

    myRobot.goto(  pos1[0], pos1[1], pos1[2] + 100, speed)

    time.sleep(1)

    myRobot.goto(  pos2[0], pos2[1], pos2[2] + 100, speed)

    time.sleep(1)

    myRobot.goto(  pos2[0], pos2[1], pos2[2] + (i + 1) * cardThickness + 2, speed)

    myRobot.pump(False)

    time.sleep(1)

    myRobot.goto(  pos2[0], pos2[1], pos2[2] + 100, speed)

    time.sleep(1)


myRobot.goto(  200, 0, 100, speed)

time.sleep(1)


#Disconnect serial connection
myRobot.disconnect()
