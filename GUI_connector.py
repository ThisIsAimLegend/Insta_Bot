#------------------------------------------------------
#Ziel-Account hier angeben
target_account = ["trichterdraws"]
#Menge der Bot Accounts hier angeben
bot_count = 3
#Menge der Bilder die einen Like bekommen sollen
like_count = 1
#Menge der Bilder die kommentiert werden sollen
comment_count = 0
#Menge der Kommentare pro Bild
comments_per_picture = 0
#ONLY WORKS WITH "comments"!!!
#Thema der Kommentare angeben
topic = "Kunst"
#------------------------------------------------------

def collectAllInputs():
    return target_account, like_count, comment_count, comments_per_picture, topic

def getBotCount():
    return bot_count