import time
from sys import exit
import test_file as tf
import insta_bot as ib

def one(target_account, bot, like_count, comment_count, cpp, topic):
    tf.open_browser()
    tf.noCookies()
    tf.FormSigner(bot)
    tf.NoPasswordSave()
    tf.NoNotifications()
    for element in target_account:
        tf.SearchAccount(element)
        tf.ClickOnAccount()
        tf.botting_actions(element,bot,topic,like_count,comment_count,cpp)
        tf.goBack()
        time.sleep(1)
    time.sleep(1)
    tf.EndProgram(bot)


def two(target_account, bot_count, like_count, comment_count, cpp, topic):
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
            ib.botting_actions(element,bot,topic,like_count,comment_count,cpp)
            ib.goBack()
            time.sleep(1)
        time.sleep(1)
        ib.EndProgram(bot)
    print("Programm fertig ausgeführt")