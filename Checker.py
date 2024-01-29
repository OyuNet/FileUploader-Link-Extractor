import os

def isLinksFileEmpty():
    file = open("links.txt", "r")
    fileData = file.readlines()

    if (len(fileData) < 1):
        return True
    else:
        return False