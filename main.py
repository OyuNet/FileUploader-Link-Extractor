from LinkExtractor import Extract
from Saver import CheckFolder, WriteData
from Remover import CheckLinksFile, RemoveLines

def main():
    CheckLinksFile()
    fileData = open("links.txt", "r").readlines()
    CheckFolder()
    
    for x in fileData:
        data = Extract(x)
        WriteData(data)
        
    RemoveLines()
    
main()