import multiprocessing
import time

from actions.structural_actions import chooseAccounts
import main
import GUI_connector as GI

def getBotList():
    bot_count = GI.getBotCount()
    bot_list = chooseAccounts(bot_count)
    return bot_list

def botProcess(n):
    target, like, comment, cpp, topic = GI.collectAllInputs()
    bot_list = getBotList()
    bot = bot_list[n]
    main.one(target, bot, like, comment, cpp, topic)

    

def ProcessManager():
    bot_list = getBotList()
    processes = []
    for i in range(len(bot_list)):
        proc = multiprocessing.Process(target=botProcess,args=(i,))
        proc.start()
        processes.append(proc)

    for process in processes:
        process.join()



if __name__ == "__main__":
    start_time = time.time()
    print("Started the program")
    ProcessManager()
    print("Finished program in",time.time()-start_time,"seconds")