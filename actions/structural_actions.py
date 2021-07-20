#import excel_actions as ea
from .excel_actions import getNumberofAccounts
from random import sample

#chooses the accounts for a given count of bots
def chooseAccounts(count):
    max_count = int(getNumberofAccounts())
    count = int(count)
    bot_list = []
    if count <= max_count:
        for i in range(count):
            n = i + 1
            bot_list.append(n)
        bot_list = sample(bot_list,len(bot_list))
        return bot_list
    else:
        raise RuntimeError("Not enough bot accounts!")
