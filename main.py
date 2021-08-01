import time
from sys import exit
import test_file as tf
from actions.structural_actions import chooseAccounts
import insta_bot as ib

#------------------------------------------------------
#Ziel-Account hier angeben
target_account = ["trichterdraws"]
#Menge der Bot Accounts hier angeben
bot_count = 1
#Menge der Bilder die einen Like bekommen sollen
like_count = 1
#Menge der Bilder die kommentiert werden sollen
comment_count = 1
#Menge der Kommentare pro Bild
comments_per_picture = 2
#ONLY WORKS WITH "comments"!!!
#Thema der Kommentare angeben
topic = "Kunst"

#------------------------------------------------------

def one():
    bot_account = chooseAccounts(bot_count)
    for bot in bot_account:
        tf.open_browser()
        tf.noCookies()
        tf.FormSigner(bot)
        tf.NoPasswordSave()
        tf.NoNotifications()
        for element in target_account:
            tf.SearchAccount(element)
            tf.ClickOnAccount()
            tf.botting_actions(element,bot,topic,like_count,comment_count,comments_per_picture)
            tf.goBack()
            time.sleep(1)
        time.sleep(1)
        tf.EndProgram(bot)
    print("Programm fertig ausgeführt")

def two():
    bot_account = chooseAccounts(bot_count)
    for bot in bot_account:
        ib.open_browser()
        ib.noCookies()
        ib.FormSigner(bot)
        ib.NoPasswordSave()
        ib.NoNotifications()
        for element in target_account:
            ib.SearchAccount(element)
            ib.ClickOnAccount()
            ib.botting_actions(element,bot,topic,like_count,comment_count,comments_per_picture)
            ib.goBack()
            time.sleep(1)
        time.sleep(1)
        ib.EndProgram(bot)
    print("Programm fertig ausgeführt")


one()
