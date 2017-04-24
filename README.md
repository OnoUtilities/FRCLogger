# ZLogger
A FRC DriverStation Logger with the purpose to
  - Retrive all NetworkTables data sent from the RoboRio and/or a coprocessor
  - Store all inputs form controllers (max of 4)
  - Allow for debug messages to be sent and stored on DriverStation

## Requirements
 **WINDOWS**:
If you want to use it just got to the [releases](http://github.com/OnoUtilities/ZLogger/releases/) page
# Usage
Use ZLogger is as simple as supplying it with a IP Address and a time offset from UTC/GMT timezone. This example below is localhost and Eastern Standnered Time GMT-04.
```cmd
ZLogger.exe localhost -4
```
Keep in mind controller need to be plugged in before running, or it won't be registered by ZLogger.
Also ZLogger only rights to files when the robot is enabled. It rights to it as a CSV file.

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
[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


 
