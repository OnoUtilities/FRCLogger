from inputs import get_gamepad as joystickEvents
import inputs
from log import Logging
import os
log = Logging()
log.createLog("Events")
log.selectLog("Events")

log.createFileLog("Events")
#log.setKeyHeader("Events", "BTN_START", "BTN_SELECT", "BTN_TR", "BTN_TL", "BTN_NORTH", "BTN_SOUTH", "BTN_WEST", "BTN_EAST", "BTN_THUMBR", "BTN_THUMBL", "ABS_RX", "ABS_RY", "ABS_X", "ABS_Y", "ABS_HAT0Y", "ABS_HAT0X", "ABS_Z", "ABZ_RZ")

log.sendMsg("Started Logging")
log.useFile(True)

while 1:
    try:
        events = joystickEvents()
        for event in events:
            if event.ev_type != 'Sync':
                log.sendMsg(event.ev_type, event.code, str(event.state))
                if event.code == "BTN_SELECT":
                    log.useFile(False)
                elif event.code == "BTN_START":
                    log.useFile(True)
                else:
                    log.addValue("Events", event.code, str(event.state))
    except KeyboardInterrupt:
        print "INTER"
        log.useFile(False)
        os._exit(0)