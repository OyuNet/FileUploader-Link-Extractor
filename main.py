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

        # Little Note to myself:
        # Maybe I could update links file in every for iteration, but I guess this thing uses much more compute power.
        # So I am going to skip that implementation. Just RemoveLines would be enough.

        RemoveLines()

main()
