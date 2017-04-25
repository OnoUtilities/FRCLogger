# Config
# Version: 1.4
# (c) 2014 Brendan Fuller
#made for Python 3, works with 2

#added edit on 2/1/2017

#Reads a tag
def read(path, variable, data):
    ConfigNumber = "****ERROR****"
    ConfigValue = "****ERROR****"
    number = 0
    path = str(path)
    file = open(path)
    f = file
    for line in f:
        number = number + 1
        var, contents = VariableReader(line)

        try:
            if var == variable:
                ConfigNumber = number
                ConfigValue = contents.strip()
        except IndexError as e:
            pass
        else:
            pass
    file.close()
    if (ConfigValue == "****ERROR****"):
        create(path, variable, data)
        ConfigValue = data
    return ConfigValue


#edits a tag
def edit(path, variable, data):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    file = open(path, "w")
    total = 0
    for line in lines:
        total = total + 1
        var, contents = VariableReader(line)
        if (var == variable):
            data = str(variable) + str("=") + str(data) + str("\n")
            file.write(data)
        else:
            file.write(line)
    file.close()


#detletes a tag
def delete(path, variable, ConfigDetail, ConfigBlankLines):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    file = open(path, "w")
    line_num = 0
    for line in lines:
        line_num = line_num + 1
        var, contents = VariableReader(line)
        try:
            if var != str(variable):
                file.write(line)
            else:
                if ConfigBlankLines == True:
                    file.write("\n")
        except IndexError as e:
            if ConfigBlankLines == True:
                file.write(line)

#creats new tag at end of file
def create(path, variable, value):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    file = open(path, "w")
    line_num_CHECK = 0
    for line in lines:
        line_num_CHECK = line_num_CHECK + 1
        if len(line) < 3:
            line = "***BLANK***"
        else:
            file.write(line)
    line_num_CHECK = line_num_CHECK + 1
    message = str(variable) + str("=") + str(value) + str("\n")
    file.write(message)
    file.close()

#creates tag at empty line (or end of file)
def create_(path, variable, value, ConfigDetail):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    file = open(path, "w")
    ConfigAppend = False
    line_num = 0
    for line in lines:
        line_num = line_num + 1
        if line != "\n" or len(line) > 3:
            file.write(line)
        else:
            if ConfigAppend == True:
                file.write(line)
            if ConfigAppend == False:
                message = str(variable) + str("=") + str(value) + str("\n")
                file.write(message)
                ConfigAppend = True
    file.close()

#reads the tag for the read function
#The was a boolean issue a long time ago, too lazy to fix
def VariableReader(line, splitter="="):
    space = " "
    text = ""
    line_Var = 0
    loop = "True"
    wait = "True"
    for letter in line:
        if loop == "True":
            if letter == space:
                break
            if letter == splitter:
                loop = "False"
                line_Var = str(text)
                text = ""
            else:
                text = str(text) + str(letter)
        if loop == "False":
            if wait == "False":
                text = str(text) + str(letter)
            else:
                wait = "False"

    return line_Var, text

#Creates a file
def createFile(name):
    file = open(name, "w")
    file.write("# Created for ZLogger\n")
    file.close


#Creates a directory
def createDirectory(name):
    import os
    if not os.path.exists(name):
        os.makedirs(name)
