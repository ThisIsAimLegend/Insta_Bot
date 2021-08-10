#import GUI

#------------------------------------------------------
#Ziel-Account hier angeben
target_account = ["ni._.na"]
#Menge der Bot Accounts hier angeben
bot_count = 2
#Menge der Bilder die einen Like bekommen sollen
like_count = 2
#Menge der Bilder die kommentiert werden sollen
comment_count = 0
#Menge der Kommentare pro Bild
comments_per_picture = 0
#ONLY WORKS WITH "comments"!!!
#Thema der Kommentare angeben
topic = ""
#------------------------------------------------------

def getGUIInput():
    #Verbindung zu GUI.py zum auslesen der Entry Widgets
    pass

def collectAllInputs():
    return target_account, like_count, comment_count, comments_per_picture, topic

def getBotCount():
    return bot_count

if __name__ == "__main__":
    getGUIInput()