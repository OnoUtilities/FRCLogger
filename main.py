#!/usr/bin/env python3
#
# This is a NetworkTables client (eg, the DriverStation/coprocessor side).
# You need to tell it the IP address of the NetworkTables server (the
# robot or simulator).
#
# This shows how to use a listener to listen for changes in NetworkTables
# values. This will print out any changes detected on the SmartDashboard
# table.
#

import sys
import time, datetime, logging
from networktables import NetworkTables
from inputs import get_gamepad as joystickEvents
from inputs import devices


from log import Logging as Log

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)


ip = "10.23.37.83"

NetworkTables.initialize(server=ip)

LOGGING = False
DEBUG_FILE = False
EVENT_FILE = False

LOGGER = Log()
LOGGER.createLog("Inputs", True)
LOGGER.createLog("NetworkTable", True)
LOGGER.createLog("DebugMessage", True)
LOGGER.createLog("Main", False)
LOGGER.selectLog("Main")




def valueChanged(key, value, isNew):
    global LOGGING
    global DEBUG_FILE
    global EVENT_FILE

    if (LOGGING == True):
        print ("[LOG] Running")
        timey = datetime.datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S.%f')[:-3]
        eData = ''.join([timey, " ", key, " ", str(value), '\n'])

        print eData
        EVENT_FILE.write(eData)
        if (key == "debugMSG"):
            DEBUG_FILE.write(eData)
    if (key == "status" and (value == "True" or value == True)):
        print ("[LOG] Passed")
        if (LOGGING == False):
            timey = datetime.datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S.%f')[:-3]
            eName = str("logs/events.") + str(timey) + str(".log")
            dName = str("logs/debug.") + str(timey) + str(".log")

            EVENT_FILE = open(eName, "w")
            DEBUG_FILE = open(dName, "w")
            LOGGING = True
    if (key == "status" and (value == "False" or value == False) and LOGGING == True):
        print ("[LOG] Closed")
        EVENT_FILE.close()
        DEBUG_FILE.close()
        LOGGING = False

    #print("valueChanged: table: '%s'; valueChanged: key: '%s'; value: %s; isNew: %s" % (table, key, value, isNew))

def connectionListener(con, info):
    connect = con;

def joystickListenr(device, id):
    try:
        gamepad = devices.gamepads[0]
    except IndexError:
        raise UnpluggedError("No gamepad found.")
    return gamepad.read()

NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

NetworkTables.addGlobalListener(valueChanged)


for device in devices.gamepads:
    thread = Thread(target=z.ShowWindow, args=(icon, title, message))
    thread.start()

while True:
    time.sleep(1)