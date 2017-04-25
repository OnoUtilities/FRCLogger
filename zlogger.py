"""
ZLogger by Import-Python (OnoUtilities)

https://github.com/OnoUtilities/ZLogger

"""




# Imports
import datetime, time, os, sys, inputs, logging
from networktables import NetworkTables
from log import Logging as Log #Custom Log Lib for CSV
from inputs import get_gamepad_id
from inputs import devices
from threading import Thread
from utils import message, resource_path, use_YES_NO, booli
import config as c

#Error Catching
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

USE_CONFIG = False
if len(sys.argv) == 2:
    if (sys.argv[1] == "true"):
        USE_CONFIG = True

if len(sys.argv) != 6 and USE_CONFIG == False:
    print("[ZLogger] Normal Usage: " + sys.argv[0] + " <ip> <utc_offset> <use_controller> <only_buttons> <debug>")
    print("[ZLogger] Config Usage: " + sys.argv[0] + " <use_config>")

    os._exit(1)

if USE_CONFIG == True:
    # Creates a config file if not already created
    file = "zlogger.config"
    try:
        settings_file = open(file, "r")
    except FileNotFoundError as e:
        c.createFile(file)
        c.create(file, "use_config", "false")
        data = use_YES_NO("[ZLogger] Do you want to use the config file option? Y/N: ")
        if (data == False):
            os._exit(1)
        c.edit(file, "use_config", "true")

        data = raw_input("[ZLogger] Robot IP [str]: ")
        c.create(file, "robot_ip", data)

        data = raw_input("[ZLogger] UTC Offset (e.g EST is -4) [int]: ")
        c.create(file, "utc_offset", data)

        c.create(file, "use_console", "false")
        use_con = use_YES_NO("[ZLogger] Do you want to log on console? Y/N: ")
        if (use_con == True):
            c.edit(file, "use_console", "true")

        c.create(file, "use_con", "false")
        use_con = use_YES_NO("[ZLogger] Do you want to log controllers? (Uses a lot more CPU) Y/N: ")
        if (use_con == True):
            c.edit(file, "use_con", "true")
        if (use_con == True):
            c.create(file, "only_btn", "false")
            use_btn = use_YES_NO("[ZLogger] Do you want to only log buttons? Y/N: ")
            if (use_btn == True):
                c.edit(file, "only_btn", "true")

        print ("[ZLogger] Please RESTART Zlogger to use config options")
        os._exit(1)
    else:
        ip = c.read(file, "robot_ip", "roborio-####-frc.local")
        offset = int(c.read(file, "utc_offset", "-4"))
        only_btn = booli(c.read(file, "only_btn", "false"))
        use_log = booli(c.read(file, "use_console", "false"))
        use_con = booli(c.read(file, "use_con", "true"))

        use_config = booli(c.read(file, "use_config", 0))

        if (use_config == False):
            print "[ZLogger] Config has been disabled! You can change it manually or use CMD args"
            print "[ZLogger] Normal Usage: " + sys.argv[0] + " <ip> <utc_offset> <use_controller> <only_buttons> <debug>"
            os._exit(1)
else:
    ip = sys.argv[1]
    offset = sys.argv[2]
    use_con = booli(sys.argv[3])
    only_btn = booli(sys.argv[4])
    use_log = booli(sys.argv[5])



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
        if (key == "/ZLogger/debugMSG"):
            L.addValue("DebugMessage", "msg", value)
    if (key == "/ZLogger/status" and (value == "True" or value == True)):
        if (LOGGING == False):
            message(resource_path("z.ico"), MAIN_NAME, "Robot Enabled")
            L.useFile(True)
            L.selectLog(MAIN_NAME)
            L.sendMsg("Logging to Files...")
            LOGGING = True
    if (key == "/ZLogger/status" and (value == "False" or value == False) and LOGGING == True):
        message(resource_path("z.ico"), MAIN_NAME, "Robot Disabled")
        L.selectLog(MAIN_NAME)
        L.sendMsg("Saving Files and adding CSV Header... Please Wait")
        L.useFile(False)
        LOGGING = False


    L.selectLog("NetworkTable")
    if (use_log):
        L.sendMsg("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))


def connectionListener(con, info):
    connect = con;

def joystickListner(device, id):
    while 1:
        try:
            events = get_gamepad_id(id)
            for event in events:
                if (event.state != "Sync" and event.code != "SYN_REPORT" and only_btn == "true"):
                    if "ABS" in event.code and only_btn == True:
                        continue
                    message = str(event.code) + str("-") + str(event.state)
                    if (use_log):
                        L.selectLog("Joystick-" + str(id))
                        L.sendMsg(message)
                    L.addValue(("JoyEvents-" + str(id)), str(event.code), str(event.state))
        except inputs.UnpluggedError as e:
            pass


L.sendMsg("ZLogger a FRC data logger by ImportPython (OnoUtilities)")
L.sendMsg("Starting Connection Listener: " + ("- " + ip))
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
L.sendMsg("Adding NT Global Listener")
NetworkTables.addGlobalListener(valueChanged)

if (use_con):
    L.selectLog(MAIN_NAME)
    L.sendMsg("Looking for Joysticks...")
    id = 0
    for device in devices.gamepads:
        L.createLog("Joystick-" + str(id))
        L.createFileLog("JoyEvents-" + str(id))
        L.selectLog(MAIN_NAME)
        L.sendMsg("Adding Joystick-" + str(id) + " Listener")
        thread = Thread(target=joystickListner, args=(device, id))
        thread.start()
        id = id + 1
    if (id == 0):
        L.selectLog(MAIN_NAME)
        L.sendMsg("No Joysticks Found!")
if (use_log == False):
    L.sendMsg("Logging has been disabled in console!")
if (only_btn):
    L.sendMsg("Joystick are only logging button presses!")
while True:
    try:
        time.sleep(0.1)
    except (KeyboardInterrupt, inputs.UnpluggedError) as e:
        L.selectLog(MAIN_NAME)
        L.sendMsg("No Joysticks Found!/Keyboard Interrupted")
        if (LOGGING == True):
          L.useFile(False)
        time.sleep(2)
        os._exit(0)