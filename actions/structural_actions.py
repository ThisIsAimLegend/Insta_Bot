#import excel_actions as ea
from .excel_actions import getNumberofAccounts
from random import sample, choice
from . import comments

#chooses the accounts for a given count of bots
def chooseAccounts(count):
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