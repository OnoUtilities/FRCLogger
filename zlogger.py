
import datetime, time, os, sys, inputs, logging
from networktables import NetworkTables
from log import Logging as Log #Custom Log Lib for CSV
from inputs import get_gamepad_id
from inputs import devices
from threading import Thread
from utils import message, resource_path

logging.basicConfig()


if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <ip> <utc_offset>")
    os._exit(1)

ip = sys.argv[1]
offset = sys.argv[2]


NetworkTables.initialize(server=ip)

LOGGING = False
MAIN_NAME = "ZLogger"

L = Log(int(offset))
L.createLog("JoyEvents")
L.createLog("NetworkTable")
L.createLog("DebugMessage")
L.createLog(MAIN_NAME)

L.selectLog(MAIN_NAME)

L.createFileLog("NetworkTable")
L.createFileLog("DebugMessage")



def valueChanged(key, value, isNew):
    global LOGGING
    if (LOGGING == True):
        L.addValue("NetworkTable", key, value)
        if (key == "/debugMSG"):
            L.addValue("DebugMessage", "msg", value)
    if (key == "/status" and (value == "True" or value == True)):
        if (LOGGING == False):
            message(resource_path("z.ico"), MAIN_NAME, "Robot Enabled")
            L.useFile(True)
            L.selectLog(MAIN_NAME)
            L.sendMsg("Logging to Files...")
            LOGGING = True
    if (key == "/status" and (value == "False" or value == False) and LOGGING == True):
        message(resource_path("z.ico"), MAIN_NAME, "Robot Disabled")
        L.selectLog(MAIN_NAME)
        L.sendMsg("Saving Files and adding CSV Header... Please Wait")
        L.useFile(False)
        LOGGING = False


    L.selectLog("NetworkTable")
    L.sendMsg("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))


def connectionListener(con, info):
    connect = con;

def joystickListner(device, id):
    while 1:
        try:
            events = get_gamepad_id(id)
            for event in events:
                if (event.state != "Sync" and event.code != "SYN_REPORT"):
                    L.selectLog("Joystick-" + str(id))
                    message = str(event.code) + str("-") + str(event.state)
                    L.sendMsg(message)
                    L.addValue(("JoyEvents-" + str(id)), str(event.code), str(event.state))
        except inputs.UnpluggedError as e:
            pass

id = 0
for device in devices.gamepads:
    L.createLog("Joystick-" + str(id))
    L.createFileLog("JoyEvents-" + str(id))
    thread = Thread(target=joystickListner, args=(device, id))
    thread.start()
    id = id + 1

L.sendMsg("ZLogger an FRC data logger by ImportPython (OnoUtilities)")
L.sendMsg("Starting Connection Listener: " + ("- " + ip))
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
L.sendMsg("Adding Global Listener")
NetworkTables.addGlobalListener(valueChanged)
while True:
    try:
        z = ""
        time.sleep(0.5)
    except (KeyboardInterrupt, inputs.UnpluggedError) as e:
        L.selectLog(MAIN_NAME)
        L.sendMsg("No Joysticks Found!/Keyboard Interrupted")
        L.useFile(False)
        time.sleep(2)
        os._exit(0)