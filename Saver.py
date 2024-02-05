# In this file, I will handle writing processes.
# My aim is write each file on different text files.
# Input is going to be [url, fileName]

import os
from Checker import isFolderExists

def CheckFile(fileName):
    path = "AppStorage/" + fileName + ".txt"
    isExists = os.path.exists(path)
     
    if (not isExists):
        open((path), "x")

def WriteData(Data):
    # Data -> [URL, fileName]
    path = "AppStorage/" + Data[1] + ".txt"
    isFolderExists()
    CheckFile(Data[1])  # Ensure the file exists
    
    with open(path, "a") as file:
        file.write(Data[0] + "\n")