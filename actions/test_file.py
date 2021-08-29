import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime as dt

import actions.excel_actions as excel
import actions.comment_actions as comments
import actions.structural_actions as structure

#closes the picture
def goBack():
    close_button = driver.find_elements_by_class_name("wpO6b")
    close_button[-1].click()

#likes every picture until there is no right arrow
def like_pictures(likes):
    for i in range(likes):
        act = ActionChains(driver)
        time.sleep(1)
        try:
            driver.find_element_by_css_selector('svg[aria-label="Gefällt mir nicht mehr"]')
        except:
            driver.find_elements_by_class_name("wpO6b")[2].click()
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

def ClickOnPicture():
    driver.find_element_by_class_name("eLAPa").click()
    time.sleep(1)


#NOT READY!!!
#sends a follow request to the targetted account
def following():
    driver.refresh()
    time.sleep(3)
    try:
        driver.find_element_by_class_name("_6VtSN").click() #y3zKF
    except:
        try:
            driver.find_element_by_class_name("y3zKF").click()
        except:
            print("Not able to follow!")
    time.sleep(0.5)

#check if already follows target account
def check_if_follow():
    try: 
        driver.find_element_by_class_name("glyphsSpriteFriend_Follow")
    except: 
        following()
    pass

#signs up into the selected bot account
def sign_up(name, pw):
    driver.find_element_by_name("username").send_keys(name)
    driver.find_element_by_name("password").send_keys(pw)
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "eGOV_"))).click()

def find_comment():
   tags = structure.getPostTags(driver)

#-------------------------------------------------------------------------------------------------
#opens the browser on www.instagram.com
def open_browser():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome("chromedriver.exe",options=options)
    driver.get("https://www.instagram.com/")
    time.sleep(0.5)
    positions = [0,960]
    pos = random.choice(positions)
    driver.set_window_position(pos,0)

#decline cookies
def noCookies():
    driver.find_element_by_class_name("bIiDR").click()
    time.sleep(0.5)

#signs into bot account
def FormSigner(bc):
    global bot_name
    name , pw = excel.getAccount(bc)
    bot_name = name
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
    time.sleep(2)

#clicks on first suggested account
def ClickOnAccount():
    click_on_account = driver.find_element_by_class_name("-qQT3")
    click_on_account.click()
    time.sleep(2)

#clicks on the latest picture on this account
def botting_actions(target,bot,topic,likes,comment_count,cpp,ll):
    try:
        select_picture = driver.find_element_by_class_name("eLAPa")
        select_picture = True
    except:
        select_picture = False
    if select_picture == True:
        check_if_follow()
        time.sleep(2)
        ClickOnStory()
        log = structure.create_log(target, bot_name, topic, likes, comment_count)
        #logger = structure.DB_Connection(ll)
        #logger.logging(target,bot_name,topic,likes,comment_count)
        if likes == None:
            pass
        else:
            ClickOnPicture()
            like_pictures(likes)
        time.sleep(0.5)
        goBack()
        time.sleep(0.5)
        if comment_count == 0:
            pass
        else:
            ClickOnPicture()
            comments.comment_loop(driver,topic,comment_count,cpp,ll)
        time.sleep(1)
        #excel.AddTargetToMemory(target,bot)
    else:
        print("No pictures found")
        check_if_follow()
        time.sleep(2)
        driver.quit()

#stops the program and closes the browser window
def EndProgram():
    driver.quit()
