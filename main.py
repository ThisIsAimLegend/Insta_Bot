import time
from sys import exit
import test_file as tf
#import insta_bot as ib
import excel_actions as ea

#------------------------------------------------------
target_account = ["montanablack"]
#Gebe die Mengae der Bot Accounts an
bot_count = 2
comments = ["lul", "xD"]
#💪
#------------------------------------------------------

def one():
    bot_account = ea.chooseAccounts(bot_count)
    for bot in bot_account:
        tf.getComments(comments)
        tf.open_browser()
        tf.noCookies()
        tf.FormSigner(bot)
        tf.NoPasswordSave()
        tf.NoNotifications()
        for element in target_account:
            tf.SearchAccount(element)
            tf.ClickOnAccount()
            tf.ClickOnStory()
            tf.ClickThroughPictures(element,bot)
            tf.goBack()
            time.sleep(1)
        time.sleep(1)
        tf.EndProgram()
    print("Bot fertig ausgeführt")

def two():
    bot_account = chooseAccounts(bot_count)
    for bot in bot_account:
        ib.getComments(comments)
        ib.open_browser()
        ib.noCookies()
        ib.FormSigner(bot)
        ib.NoPasswordSave()
        ib.NoNotifications()
        for element in target_account:
            ib.SearchAccount(element)
            ib.ClickOnAccount()
            ib.ClickOnStory()
            ib.ClickThroughPictures(element,bot)
            ib.goBack()
            time.sleep(1)
        time.sleep(1)
        ib.EndProgram()
    print("Bot fertig ausgeführt")


one()
