import threading
import time

from actions.structural_actions import chooseAccounts
import main
import GUI_connector as GI

start_time = time.time()

def getBotList():
    global bot_list
    bot_count = GI.getBotCount()
    bot_list = chooseAccounts(bot_count)

def botProcess(n):
    target, like, comment, cpp, topic = GI.collectAllInputs()
    bot = bot_list[n-1]
    main.one(target, bot, like, comment, cpp, topic)

class ThreadManager(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        #Hier die Multithreading-Aktionen einfügen
        time.sleep(self.id*2)
        botProcess(self.id)


#Versuche zuerst ein dictionary für alle threads zu erstellen und sie danach zu starten und zu joinen
getBotList()
bot_count = len(bot_list)
ThreadList = {}
n = 1
for bot in range(1,bot_count+1):
    key = "Bot" + str(n)
    value = ThreadManager(n)
    ThreadList[key] = value
    n += 1 

print(ThreadList)

for i in ThreadList.keys():
    BotThread = ThreadList[i]
    BotThread.start()
    
  
for i in ThreadList.keys():
    BotThread = ThreadList[i]
    BotThread.join()
  
print("Programm fertig ausgeführt in:",(time.time() - start_time))