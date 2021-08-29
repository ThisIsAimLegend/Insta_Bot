import datetime as dt
from random import sample, choice
from . import comments
import mariadb
import sys
import keyring

#chooses the accounts for a given count of bots
def chooseAccounts(count):
    from .excel_actions import getNumberofAccounts
    max_count = int(getNumberofAccounts())
    count = int(count)
    if count <= max_count:
        possible_bots = list(range(1,max_count+1))
        sample(possible_bots,len(possible_bots))
        bot_list = []
        for i in range(count):
            n = choice(possible_bots)
            bot_list.append(n)
            possible_bots.remove(n)
        bot_list = sample(bot_list,len(bot_list))
        return bot_list
    else:
        raise RuntimeError("Not enough bot accounts!")

def getPostTags(driver):
    try:
        driver.find_elements_by_class_name("xil3i")
        
    except:
        print("No hastags found")
        pass

    tags = driver.find_elements_by_class_name("xil3i")
    i = 0
    tag_list = []
    for tag in tags:
        item = tag.text
        tag_list.append(item)
        i += 1
    print(tag_list)
    return tag_list

#creates the log as a list
def create_log(target,bot_name, topic, like_count, comment_count):
    timer = dt.datetime.now()
    timer = timer.strftime("[%d.%m.%Y , %H:%M:%S]")
    log = []
    log.append(timer)
    log.append("Ziel: " + str(target))
    log.append("Bot: " + str(bot_name))
    log.append("Pictures liked: " + str(like_count))
    log.append("Comments posted: " + str(comment_count))
    log.append("Comment topic: " + str(topic))
    print(log)
    log = (target,bot_name,topic,like_count,comment_count)
    return log

class DB_Connection:
    def __init__(self,logLock):
        connection = mariadb.connect(
                user="root",
                password=keyring.get_password("databank","root"),
                host="localhost",
                port=3306,
                database="InstaBot"
            )
        cur = connection.cursor()

        self.connection = connection
        self.cur = cur
        self.logLock = logLock

    def logging(self,target,bot_name, topic, like_count, comment_count):
        if self.logLock != None:
            self.logLock.acquire()
        self.cur.execute("INSERT INTO log (target,bot,likes,comments,topic) VALUES (?,?,?,?,?)",(target,bot_name,like_count,comment_count,topic))
        self.connection.commit()
        self.connection.close()
        if self.logLock != None:
            self.logLock.release()

if __name__ == "__main__":
    pass