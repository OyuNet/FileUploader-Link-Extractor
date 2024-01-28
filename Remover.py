import os

def CheckLinksFile():
    isExists = os.path.exists("links.txt")
    
    if (not isExists):
        print("Your links.txt file is not exists. New one created.")
        file = open("links.txt", "x")
        
def RemoveLines():
    file = open("links.txt", "w")
    file.write("") # Now entire file content erased.