# ZLogger
A FRC DriverStation Logger with the purpose to
  - Retrive all NetworkTables data sent from the RoboRio and/or a coprocessor
  - Store all inputs form controllers (max of 4)
  - Allow for debug messages to be sent and stored on DriverStation

## Requirements
 **WINDOWS**:
If you want to use it just got to the [releases](http://github.com/OnoUtilities/ZLogger/releases/) page
**LINUX/MAC**:
You can look at building requirements, but keep in mind ```pywin32``` is bein used.
# Usage
 **WINDOWS**:
Using ZLogger on Windows s as simple as supplying it with a IP Address and a time offset from UTC/GMT timezone. This example below is ````roborio-####-frc.local```` and Eastern Standnered Time (GMT-4).
```cmd
ZLogger.exe roborio-####-frc.local -4
```
Keep in mind controller(s) need to be plugged in before running, or it won't be registered by ZLogger.
Also ZLogger only rights to files when the robot is enabled. It rights to it as a CSV file.

 **ROBOT**:
 The robot has to include some code as well. If your using Java you can use the simple 
 ZLogger.java class as shown below. If you are using LabView, RobotPy or C, here a brief overview.
 In NetworkTables do the following when:
 - **AUTON ENABLED** 
            - Make ```/ZLogger/status``` to ```true```
            - Make ```/ZLogger/type``` to ```auton```
 - **TELEOP ENABLED** 
            - Make ```/ZLogger/status``` to ```true```
            - Make ```/ZLogger/type``` to ```teleop```
 - **DISABLED** 
            - Make ```/ZLogger/status``` to ```false```
            - Make ```/ZLogger/type``` to ```none```
 - **DEBUGS MESSAGE** Make ```/ZLogger/debugMSG``` to ```<message>``` (optional)

##### ZLogger Library (Java):
 ***WILL BE ADDED SOON***
# Running/Building:
- Requires Python2.7
- These Library's:  ```inputs``` , ```pywin32``` 
- And if you want to build the exe you need: ```pyinstaller``` 
### Running
To run drag all files into a directory of choice then run:
```cmd
py zlogger.py localhost -4
```
### Pyintaller Building:
This is the command argument used for building the exe (64 bit) via the spec file.
```bash
pyinstaller.exe zlogger.spec --onefline -F
```  
# Upcoming Features:
* Thing of more fetures?
# About
This was made for logging various anything that NetworkTables could  send. Also controllers are nice to have as well to see if someone hit the wrong button.

# Credits
Thanks to [this image and author](https://www.iconfinder.com/icons/199213/extension_file_format_log_icon#size=128) for a nice icon file.
