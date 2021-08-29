import multiprocessing
import time

from actions.structural_actions import chooseAccounts
import actions.main as main


#imports the Botlist for process division and bot signing
def getBotList(bot_count):
    bot_list = chooseAccounts(bot_count)
    return bot_list

#redirects the created bots to their actions
def botProcess(bot,logLock,target,like,comment,cpp,topic):
    main.experimental(target, bot, like, comment, cpp, topic, logLock)

def ProcessManager(acc, bot_num, like_num, com_num, cpp,topic):
    bot_num = int(bot_num)
    like_num = int(like_num)
    com_num = int(com_num)
    cpp = int(cpp)
    start_time = time.time()
    logManager = multiprocessing.Manager()
    logLock = logManager.Lock()
    bot_list = getBotList(bot_num)
    if bot_num <= 3:
        procs = bot_num
    else:
        procs = 3
    pool = multiprocessing.Pool(processes=procs)
    for bot in bot_list:
        pool.apply_async(botProcess,[bot,logLock,acc,like_num,com_num,cpp,topic])
    time.sleep(1)
    pool.close()
    pool.join()
    print("Finished bots in",time.time()-start_time,"seconds")

if __name__ == "__main__":
    start_time = time.time()
    print("Started the program")
    ProcessManager()
    print("Finished program in",time.time()-start_time,"seconds")