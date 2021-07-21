from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard
import datetime as dt

import actions.excel_actions as ea

def getComments(c):
    global comment
    comment = c

def goBack():
    #print("Go back")
    keyboard.press_and_release("esc")

def like_pictures():
    while True:
        driver.find_element_by_class_name("fr66n").click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        except:
            print("Fertig")
            break
        time.sleep(1)

def ClickOnStory():
    story = driver.find_element_by_class_name("_6q-tv")
    story.click()
    time.sleep(1)
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
    keyboard.press_and_release("tab")
    time.sleep(0.5)
    keyboard.press_and_release("tab")
    time.sleep(0.5)
    keyboard.press_and_release("enter")

#signs up into the selected bot account
def sign_up(name, pw):
    driver.find_element_by_name("username").send_keys(name)
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_class_name("eGOV_").click()

#posts all given comments on the first post
def send_comment():
    for i in comment:
        commentary = driver.find_element_by_css_selector('textarea[aria-label="Kommentar hinzufügen ..."]')
        commentary.click()
        time.sleep(0.5)
        keyboard.write(i)
        keyboard.press_and_release("Enter")
        time.sleep(1)

#opens the browser on www.instagram.com
def open_browser():
    global driver
    driver = webdriver.Chrome("D:\Programme\learn_coding\Selenium\chromedriver.exe")
    driver.get("https://www.instagram.com/")
    time.sleep(0.5)
    driver.maximize_window()

#decline cookies
def noCookies():
    driver.find_element_by_class_name("bIiDR").click()
    time.sleep(0.5)

#signs into bot account
def FormSigner(bc):
    name , pw = ea.getAccount(bc)
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
def ClickThroughPictures(target,bot):
    bot_memory = ea.SearchForAccount(target,bot)
    if bot_memory == False:
        #following()
        try:
            select_picture = driver.find_element_by_class_name("eLAPa")
            select_picture = True
        except:
            select_picture = False
        if select_picture == True:
            driver.find_element_by_class_name("eLAPa").click()
            time.sleep(2)
            timer = dt.datetime.now()
            timer = timer.strftime("[%H:%M:%S %d.%m.%Y]")
            print(timer)
            print("Ziel:",target)
            print("Bot:",bot,"\n")
            like_pictures()
            time.sleep(1)
            ea.AddTargetToMemory(target,bot)
        else:
            driver.quit()
    elif bot_memory == True:
        pass
    else:
        print("Fehler beim Auslesen der Accountliste")

def EndProgram():
    driver.quit()
