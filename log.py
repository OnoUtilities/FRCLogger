"""
Log > Logger
by Import-Python

-- It's a simple logger because yeah!
-- Adds key based csv support (without CSV lib)

"""
from datetime import datetime
from datetime import tzinfo, timedelta
import os, calendar, collections
import time, fileinput, csv

class Logging:
    def __init__(self, utc_offset):
        self.main_log_list = {}
        self.file_log_list = {}

        self.file_log_header = {}

        self.main_log_title = ""
        self.file_log_title = ""

        self.file_log_path = {}

        self.files_list = {}
        self.file_open = {}
        self.file_sub = {}

        self.file_use = False

        self.file_data = {}
        self.file_data = collections.defaultdict(list)


        self.log_folder = "logs"
        self.time_zone = Zone(utc_offset,False,'EST')
    #-----------------------------------------------------------------------------
    """
          Create a log
          @param name - NAME OF LOG
    """
    def createLog(self, name):
        if name not in self.main_log_list:
            self.main_log_list[name] = name
        else:
            self.__sendErrorMsg("Logger '" + name + "' already created!")
    """
          Create a file log
          @param name - NAME OF LOG
    """
    def createFileLog(self, name, sub=None):
        if sub is None:
            sub = ""
        if name not in self.file_log_list:
            self.file_log_list[name] = name
            self.file_open[name] = False
            self.file_log_header[name] = []
            self.file_sub[name] = sub
        else:
            self.__sendErrorMsg("Logger '" + name + "' already created!")
    """
        Selects a log
        @param name - NAME OF LOG
    """
    def selectLog(self, name):
        if name in self.main_log_list:
            self.main_log_title = name

    # -----------------------------------------------------------------------------
    """
          Sends a message
          @param msg - MESSAGE
    """
    def sendMsg(self, *args):
        for arg in args:
            message = str("[") + str(self.__getTime()) + str("][") + str(self.main_log_title) + str("] ") + str(arg)
            print (message)

    """
         addValue(<log name>, <key [col]>, <value>)

         This is for a file based log. It adds a key (or a column if viewed via a CSV viewer)

         <log name>  = The log name
         <key [col]> = Key or column name for value
         <value> = Data for that key

         {time [row]} = Auto

    """
    def addValue(self, name, key, value):
        if name in self.file_log_list:
            data = str("\"") + str(self.__getTime()) + str ("\",\"") + str(name) + str("\",")
            if self.file_use == True:
                self.file_open[name] = True
                found = False
                for col in self.file_log_header[name]:
                    if col == key:
                        found = True
                        data = str(data) + str("\"") + str(value) + str("\"")
                    else:
                        data = str(data) + str(",")
                if found == False:
                    self.file_log_header[name].append(key)
                    self.addValue(name, key, value)
                else:
                    data = str(data) + str("\n")
                    self.files_list[name].write(data)
        else:
            self.__sendErrorMsg("Logger '" + name + "' is invaild!")

    # -----------------------------------------------------------------------------

    """
        useFile(<boolean>)

        Do you want to start logging file logs?
        Well useFile(true) enables logging and when you want to stop
        just do useFile(false)
    """
    def useFile(self, boolean):
        self.file_use = boolean
        if boolean == True:
            for key, value in self.file_log_list.iteritems():
                dir_path = str(self.log_folder) + str("/") + str(self.__getSafeYMD()) + str("/") + str(key) + str("/")
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                file_path = str(dir_path) + str(self.__getSafeTime()) + str(".csv")
                self.files_list[key] = open(file_path, "w")
                self.file_log_path[key] = file_path
                #self.files_list[key].write("HEADER\n\n")
        if boolean == False:
            for key, value in self.files_list.iteritems():
                header = str("Time,Log,")
                self.files_list[key].close()
                time.sleep(1)
                for col in self.file_log_header[key]:
                    header = str(header) + str(col) + str(",")
                header = str(header) + str("")
                self.__sendLogMsg("Adding Header: " + self.file_log_path[key])
                self.__line_prepender(self.file_log_path[key], header)

    """ GRABS A LOGS TITLE"""
    def getLog(self):
        return self.main_log_title

    """ PRIVATE FUNCTIONS"""
    def __sendErrorMsg(self, message):
        old = self.getLog()
        self.main_log_title = "Error"
        self.sendMsg(message)
        self.main_log_title = old

    def __sendLogMsg(self, message):
        old = self.getLog()
        self.main_log_title = "Log"
        self.sendMsg(message)
        self.main_log_title = old

    """ Timed Based Functions"""
    def __getTime(self):
        return datetime.now(self.time_zone).strftime('%m/%d/%Y %I:%M:%S.%f')[:-3]
    def __getSafeTime(self):
        return datetime.now(self.time_zone).strftime('%m_%d_%Y=%I_%M_%S_%f')[:-3]
    def __getSafeYMD(self):
        return datetime.now(self.time_zone).strftime('%m_%d_%Y')

    """ Adds a line to top of file, used for header of CSV"""
    def __line_prepender(self, path, header):
        with open(path, 'r+') as f:
            # Read header
            # Read complete data of CSV file
            old = f.read()
            # Get cursor to start of file
            f.seek(0)
            # Write header and old data to file.
            f.write(header + "\n" + old)




#Grabs proper time zone (via offset)
class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name
"""
EXAMPLE
log = Logging()
log.createLog("Inputs")
log.createLog("NetworkTable")
log.createFileLog("Joystick-1")

log.selectLog("Inputs") #Normal log
logs.useFile(True) #Enables file catching
log.addValue("Joystick-1", "KEY", "VALUE") #File log - adds value (as a column) and if not created adds it.
log.addValue(####) #and so on
log.useFile(False) #Save file and adds header based on keys
"""