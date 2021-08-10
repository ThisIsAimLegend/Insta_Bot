import time
from sys import exit
import test_file as tf
import insta_bot as ib

def experimental(target_account, bot, like_count, comment_count, cpp, topic, ll):
    tf.open_browser()
    tf.noCookies()
    tf.FormSigner(bot)
    tf.NoPasswordSave()
    tf.NoNotifications()
    for element in target_account:
        tf.SearchAccount(element)
        tf.ClickOnAccount()
        tf.botting_actions(element,bot,topic,like_count,comment_count,cpp,ll)
        tf.goBack()
        time.sleep(1)
    time.sleep(1)
    tf.EndProgram(bot)


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
    tf.FormSigner(bot)
    tf.NoPasswordSave()
    tf.NoNotifications()
    tf.SearchAccount(target_account)
    tf.ClickOnAccount()
    tf.ClickOnPicture()
    tf.like_pictures(like_count)
    tf.EndProgram(bot)