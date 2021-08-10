import multiprocessing
import time

from actions.structural_actions import chooseAccounts
import main
import GUI_connector as GI

#imports the Botlist for process division and bot signing
def getBotList():
    bot_count = GI.getBotCount()
    bot_list = chooseAccounts(bot_count)
    return bot_list

#redirects the created bots to their actions
def botProcess(bot,logLock):
    target, like, comment, cpp, topic = GI.collectAllInputs()
    main.bot(target, bot, like, comment, cpp, topic, logLock)

def ProcessManager():
    logManager = multiprocessing.Manager()
    logLock = logManager.Lock()
    bot_list = getBotList()
    pool = multiprocessing.Pool(processes=3)
    for bot in bot_list:
        pool.apply_async(botProcess,[bot,logLock])
    pool.close()
    pool.join()

'''
#creates an independent process for every bot in the botlist
def ProcessManager():
    logLock = multiprocessing.Lock()
    bot_list = getBotList()
    processes = []
    for i in range(len(bot_list)):
        proc = multiprocessing.Process(target=botProcess,args=(i,logLock))
        proc.start()
        processes.append(proc)

    for process in processes:
        process.join()
'''


if __name__ == "__main__":
    start_time = time.time()
    print("Started the program")
    ProcessManager()
    print("Finished program in",time.time()-start_time,"seconds")