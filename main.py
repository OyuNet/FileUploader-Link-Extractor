from LinkExtractor import Extract
from Saver import WriteData
from Remover import RemoveLines
from Checker import isLinksFileEmpty, isFolderExists, isLinksFileExists

def main():
    isLinksFileExists()

    if (isLinksFileEmpty()):
        print("Your links.txt file is empty. Fill it with your desired log lines to proceed.")
    else:
        fileData = open("links.txt", "r").readlines()
        isFolderExists()

        for x in fileData:
            data = Extract(x)
            WriteData(data)

        RemoveLines()

main()
