import os

def isLinksFileEmpty():
    file = open("links.txt", "r")
    fileData = file.readlines()

    if (len(fileData) > 0):
        return False
    else:
        return True

def isFolderExists():
    isExists = os.path.exists("AppStorage")

    if (not isExists):
        os.mkdir("AppStorage")

def isLinksFileExists():
    isExists = os.path.exists("links.txt")

    if (not isExists):
        print("Your links.txt file is not exists. New one created.")
        file = open("links.txt", "x")
