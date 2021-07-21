import random

global topic_list
topic_list = ["Fußball","Weiber","comments"]

def getTopic(topic):
    str(topic)
    if topic in topic_list:
        return topic
    else:
        print("Topic not found")
        return None

def pickRandomEmoji():
    emoji_list = ["💪🏼","🔥","👌🏼"]
    emoji = random.choice(emoji_list)
    return emoji

def PickRandomComment(topic):
    topic = getTopic(topic)
    path = "./actions/comments/"+topic+".txt"
    file = open(path,"r")
    data = file.read()
    data = data.split("\n")
    comment = random.choice(data)
    str(comment)
    return comment

def returnFullComment(topic):
    comment = str(PickRandomComment(topic))
    emoji = str(pickRandomEmoji())
    full_comment = comment + emoji
    print(full_comment)
    return full_comment