import random
from . import comments

def chooseComments(topic):
    comDict = comments.comDict
    i = 0
    for t in comDict["topic_index"]:
        if t == topic:
            topicDict = comDict["topic"][i]
            continue
        else:
            i += 1
        
    tags = topicDict.keys()
    comment_list = []
    for i in tags:
        comment_list.append(i)
    return comment_list

def PickRandomComment(topic):
    comment_list = chooseComments(topic)
    comment = random.choice(comment_list)
    if comment != "":
        return comment
    else:
        return None

def pickRandomEmoji(topic):
    if topic == "Freunde":
        emoji_list = comments.comDict["Freunde_emoji"]
    elif topic == "Girls":
        emoji_list = comments.comDict["Girls_emoji"]
    elif topic == "Sport":
        emoji_list = comments.comDict["Sport_emoji"]
    elif topic == "Influencer":
        emoji_list = comments.comDict["Influencer_emoji"]
    elif topic == "Kunst":
        emoji_list = comments.comDict["Kunst_emoji"]
    else:
        print("Type a topic that already exists!")
        return ""
    emoji = random.choice(emoji_list)
    return emoji
    

def returnFullComment(topic):
    comment = PickRandomComment(topic)
    if comment == None:
        pass
    else:
        str(comment)
        emoji = str(pickRandomEmoji(topic))
        full_comment = comment + emoji
        print(full_comment)
        return full_comment