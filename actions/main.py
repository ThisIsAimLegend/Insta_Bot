import time
from sys import exit
import actions.test_file as tf
import actions.insta_bot as ib

#NOT WORKING!!!
def experimental(target_account, bot, like_count, comment_count, cpp, topic, ll):
    try:
        tf.open_browser()
        tf.noCookies()
        tf.FormSigner(bot,ll)
        tf.NoPasswordSave()
        tf.NoNotifications()
        for element in target_account:
            tf.SearchAccount(element)
            tf.ClickOnAccount()
            tf.botting_actions(element,bot,topic,like_count,comment_count,cpp,ll)
            tf.goBack()
            time.sleep(1)
        time.sleep(1)
        tf.EndProgram()
        print("Bot",bot,"fertig")
    except:
        print("Bot",bot,"failed")
        tf.EndProgram()
        


def bot(target_account, bot, like_count, comment_count, cpp, topic, ll):
    ib.open_browser()
    ib.noCookies()
    ib.FormSigner(bot)
    ib.NoPasswordSave()
    ib.NoNotifications()
    for element in target_account:
        ib.SearchAccount(element)
        ib.ClickOnAccount()
        ib.botting_actions(element,bot,topic,like_count,comment_count,cpp,ll)
        ib.goBack()
        time.sleep(1)
    time.sleep(1)
    ib.EndProgram(bot)

def test(target_account, bot, like_count, comment_count, cpp, topic, ll):
    tf.open_browser()
    tf.noCookies()
    tf.FormSigner(bot,ll)
    tf.NoPasswordSave()
    tf.NoNotifications()
    for element in target_account:
        tf.SearchAccount(element)
        tf.ClickOnAccount()
        tf.botting_actions(element,bot,topic,like_count,comment_count,cpp,ll)
        tf.goBack()
        time.sleep(1)
    tf.EndProgram()