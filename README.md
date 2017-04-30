# ZLogger
A FRC DriverStation Logger with the purpose to
  - Retrive all NetworkTables data sent from the RoboRio and/or a coprocessor
  - Store all inputs form controllers (max of 4)
  - Allow for debug messages to be sent and stored on DriverStation

## Requirements
 **WINDOWS**:

If you want to use it just got to the [releases](http://github.com/OnoUtilities/ZLogger/releases/) page

**ROBORIO**:

If you use Java, you can look [here](https://github.com/OnoUtilities/ZLogger/wiki/ZLogger-Java-Lib)
If you don't use Java, you can look [here](https://github.com/OnoUtilities/ZLogger/wiki/NetworkTable-and-ZLogger)
# Usage
Use ZLogger is as simple as supplying it with a IP Address, a time offset from UTC/GMT timezone, if you want to use a controller, and if so log only buttons plus a debug stream (spam console or no?).
```cmd
NORMAL USAGE: ZLogger.exe <ip> <utc_offset> <use_controller> <only_buttons> <debug>
CONFIG USAGE: ZLogger.exe <use_config>
```
Also there is a config option, so if you say `true` for it, it will ask you to enter option in the command prompt.

Keep in mind controller need to be plugged in before running, or it won't be registered by ZLogger.
Also ZLogger only rights to files when the robot is enabled. It rights to it as a CSV file.

# Building:

If you want to build it you can take a look at the [build section](https://github.com/OnoUtilities/ZLogger/wiki/Building-ZLogger)

# Upcoming Features:
* Think of more fetures?

# About
This was made for logging various anything that NetworkTables could  send. Also controllers are nice to have as well to see if someone hit the wrong button.

# Credits
Thanks to [this image and author](https://www.iconfinder.com/icons/199213/extension_file_format_log_icon#size=128) for a nice icon file.
