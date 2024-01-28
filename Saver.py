# In this file, I will handle writing processes.
# My aim is write each file on different text files.
# Input is going to be [url, fileName]

import os

def CheckFile(fileName):
    path = "AppStorage/" + fileName + ".txt"
    isExists = os.path.exists(path)
     
    if (not isExists):
        open((path), "x")

def CheckFolder():
    # In this function, I will handle folder existence.
    # If folder not exists, function gonna be create new folder.
    
    isExists = os.path.exists("AppStorage")
    
    if (not isExists):
        os.mkdir("AppStorage")

def WriteData(Data):
    # Data -> [URL, fileName]
    path = "AppStorage/" + Data[1] + ".txt"
    CheckFolder()  # Ensure the folder exists
    CheckFile(Data[1])  # Ensure the file exists
    
    with open(path, "a") as file:
        file.write(Data[0] + "\n")