#import excel_actions as ea
from .excel_actions import getNumberofAccounts
from random import sample, choice

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