# In this file, I will handle extraction processes.
# Just only one line will considered.
# Separation thing should be on main.py I guess.
# Example Log Line: 2024-01-28 00:06:04|vidshar.org|https://cdn2.vadsr.shop/maxz38snwlzv.html||[YuushaSubs]  Puzzle and Dragons Cross - 09.mp4|

def Extract(line: str):
    # First Line: Upload Date
    # Second Line: Server Domain
    # Third Line: URL
    # Fourth Line: File Name
    # I will just use third and fourth line.
    
    try:
        url = line.split("|")[2]
        fileName = line.split("|")[4]
        return [url, fileName]
    except:
        print("Wrong log line encountered: {}".format(line))
        return ["null", "null"]