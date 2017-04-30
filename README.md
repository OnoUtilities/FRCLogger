# ZLogger
A FRC DriverStation Logger with the purpose to
  - Retrive all NetworkTables data sent from the RoboRio and/or a coprocessor
  - Store all inputs form controllers (max of 4)
  - Allow for debug messages to be sent and stored on DriverStation

## Requirements
 **WINDOWS**:
If you want to use it just got to the [releases](http://github.com/OnoUtilities/ZLogger/releases/) page
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
- Requires Python2.7
- These libs:  ```inputs``` , ```pywin32``` 
- And if you want to build the exe you need: ```pyinstaller``` 

### Pyintaller Building:
This is the command argument used for building the exe (64 bit) via the spec file.
```bash
pyinstaller.exe zlogger.spec --onefline -F
```
### Linux/OSX
This was made for Windows, becasuse the DriverStation (or legal FMS one) only runs on it. Now it 'should' work. It does use pywin32 for BallonTip messages (enabled robot, disabled robot) but other than that it 'should' work.

# Upcoming Features:
* Think of more fetures?

# About
This was made for logging various anything that NetworkTables could  send. Also controllers are nice to have as well to see if someone hit the wrong button.

# Credits
Thanks to [this image and author](https://www.iconfinder.com/icons/199213/extension_file_format_log_icon#size=128) for a nice icon file.
