import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import keyboard
import datetime as dt

import actions.excel_actions as excel
import actions.comment_actions as comments
import actions.structural_actions as structure


#closes the picture
def goBack():
    #print("Go back")
    keyboard.press_and_release("esc")

#likes every picture until there is no right arrow
def like_pictures(likes):
    for i in range(likes):
        act = ActionChains(driver)
        like = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME,'ZyFrc')))
        act.double_click(like).perform()
        time.sleep(0.5)
        try:
            driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        except:
            print("Like auf allen Bildern hinzugefügt")
            break
        time.sleep(1)

#clicks through the stories if they exist
def ClickOnStory():
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME,'_6q-tv'))).click()
    time.sleep(3)
    while True:
        try:
            driver.find_element_by_class_name("K_10X")
            next = driver.find_element_by_class_name("coreSpriteRightChevron")
            next.click()
        except:
            break
        time.sleep(1)


#NOT READY!!!
#sends a follow request to the targetted account
def following():
    keyboard.press_and_release("f5")
    time.sleep(3)
    keyboard.press_and_release("tab")
    time.sleep(0.1)
    keyboard.press_and_release("tab")
    time.sleep(0.1)
    keyboard.press_and_release("enter")
    time.sleep(0.5)

#signs up into the selected bot account
def sign_up(name, pw):
    driver.find_element_by_name("username").send_keys(name)
    driver.find_element_by_name("password").send_keys(pw)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "eGOV_"))).click()

def find_comment():
   tags = structure.getPostTags(driver)

#posts random comment from topic list
def send_comment(topic):
    comment = comments.returnFullComment(topic)
    if comment == None:
        pass
    else:
        time.sleep(1)
        driver.find_element_by_css_selector('textarea[aria-label="Kommentar hinzufügen ..."]').click()
        time.sleep(0.5)
        keyboard.write(comment)
        keyboard.press_and_release("Enter")
        time.sleep(1)

#creates the log as a list
def create_log(target, bot):
    timer = dt.datetime.now()
    timer = timer.strftime("[%d.%m.%Y , %H:%M:%S]")
    log = []
    log.append(timer)
    log.append("Ziel: " + str(target))
    log.append("Bot: " + str(bot))
    return log
    
#creates a log in "bot_log.txt"
def logging(log):
    print(log)
    file = open("data/bot_log.txt","a")
    file.write("\n")
    for row in log:
        file.write(row)
        file.write("\n")
    file.close()

#-------------------------------------------------------------------------------------------------
#opens the browser on www.instagram.com
def open_browser():
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.instagram.com/")
    time.sleep(0.5)
    driver.maximize_window()

#decline cookies
def noCookies():
    driver.find_element_by_class_name("bIiDR").click()
    time.sleep(0.5)

#signs into bot account
def FormSigner(bc):
    name , pw = excel.getAccount(bc)
    sign_up(name, pw)
    time.sleep(4)

#Decline saving the password
def NoPasswordSave():
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "yWX7d"))).click()
    time.sleep(0.5)

#Don't accept notifications
def NoNotifications():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "HoLwm"))).click()
    time.sleep(0.5)

#searches for targetted account
def SearchAccount(target_account):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[placeholder="Suchen"]'))).send_keys(target_account)
    time.sleep(1)

#clicks on first suggested account
def ClickOnAccount():
    click_on_account = driver.find_element_by_class_name("-qQT3")
    click_on_account.click()
    time.sleep(2)

#clicks on the latest picture on this account
def botting_actions(target,bot,topic,likes):
    try:
        select_picture = driver.find_element_by_class_name("eLAPa")
        select_picture = True
    except:
        select_picture = False
    if select_picture == True:
        ClickOnStory()
        driver.find_element_by_class_name("eLAPa").click()
        time.sleep(2)
        log = create_log(target,bot)
        logging(log)
        find_comment()
        if likes == None:
            pass
        else:
            like_pictures(likes)
        time.sleep(1)
        excel.AddTargetToMemory(target,bot)
    else:
        following()
        time.sleep(2)
        driver.quit()

#stops the program and closes the browser window
def EndProgram(bot):
    print("Bot",bot,"fertig")
    driver.quit()
