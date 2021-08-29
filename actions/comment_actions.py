import random
import time
import keyboard
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
    return comment

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
    elif topic == "Musik":
        emoji_list = comments.comDict["Musik_emoji"]
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
        #print(full_comment)
        return full_comment


#posts random comment from topic list
def send_comment(driver,topic,cpp,logLock):
    comment_test = returnFullComment(topic)
    if comment_test == None:
        pass
    else:
        for _ in range(cpp):
            comment = returnFullComment(topic)
            print(comment)
            time.sleep(0.5)
            #driver.find_element_by_css_selector('textarea[aria-label="Kommentar hinzufügen ..."]').click()
            driver.find_element_by_class_name("Ypffh").click()
            time.sleep(0.5)
            if logLock != None:
                logLock.acquire()
            driver.switch_to_window(driver.current_window_handle)
            keyboard.write(comment)
            keyboard.press_and_release("Enter")
            if logLock != None:
                logLock.release()
            time.sleep(1)

def comment_loop(driver,topic,comment_count,cpp,ll):
    for _ in range(comment_count):
        send_comment(driver,topic,cpp,ll)
        time.sleep(0.5)
        try:
            driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        except:
            break
        time.sleep(1)
    print("Alle Kommentare abgeschickt")