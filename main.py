from LinkExtractor import Extract
from Saver import CheckFolder, WriteData
from Remover import CheckLinksFile, RemoveLines
from Checker import isLinksFileEmpty

def main():
    CheckLinksFile()
    
    if (isLinksFileEmpty):
        print("Your links.txt file is empty. Fill it with your desired log lines to proceed.")
    else:
        fileData = open("links.txt", "r").readlines()
        CheckFolder()
        
        for x in fileData:
            data = Extract(x)
            WriteData(data)
            
        RemoveLines()
    
main()