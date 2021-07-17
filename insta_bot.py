from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import keyboard

def getComments(c):
    global comment
    comment = c

def goBack():
    #print("Go back")
    keyboard.press_and_release("esc")
    time.sleep(1)

#account-details for logging into the account
def account1():
    global name, pw
    name = "test.mail.trichter@gmail.com"
    pw = "test.python"

def account2():
    global name, pw
    name = "checkmeout1337@gmail.com"
    pw = "41KKIZ6h8JReWyxzlkSL"

def account3():
    global name, pw
    name = "doublixah"
    pw = "test.python"
    try:
        f = open("like_3","a")
        f.close()
    except:
        open("like_3","w+")
        f.close()

def account4():
    global name, pw
    name = "candicejokenotfunny420"
    pw = "test.python"
    try:
        f = open("like_4","a")
        f.close()
    except:
        open("like_4","w")
        f.close()

def like_pictures():
    while True:
        driver.find_element_by_class_name("fr66n").click()
        send_comment()
        time.sleep(1)
        try:
            driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        except:
            break
        time.sleep(1)

class FileOpener:
    global data
    def read(self,bot_account):
        if bot_account == 1:
             return open("like","r")
        elif bot_account == 2:
            return open("like_2","r")
        elif bot_account == 3:
            return open("like_3","r")
        elif bot_account == 4:
            return open("like_4","r")
        else:
            raise RuntimeError("Fehler beim öffnen der Datei")
    def write(self,bot_account):
        if bot_account == 1:
            return open("like","a")
        elif bot_account == 2:
            return open("like_2","a")
        elif bot_account == 3:
            return open("like_3","a")
        elif bot_account == 4:
            return open("like_4","a")
        else:
            raise RuntimeError("Fehler beim Öffnen der Datei")

openFile = FileOpener()

def changeFile(acc,bot_account):
    acc = str(acc)
    data = openFile.write(bot_account)
    data.write(acc)
    data.write("\n")

def readOutFile(target_account,bot_account):
    data = openFile.read(bot_account)
    datasheet = data.read()
    if target_account in datasheet:
        print("Gefunden:",target_account)
    else:
        print("Like-Bot wird ausgeführt für:",target_account)
        changeFile(target_account,bot_account)
        like_pictures()

    data.close()

def sign_up():
    driver.find_element_by_name("username").send_keys(name)
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_class_name("eGOV_").click()

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
    if bc == 1:
        account1()
    elif bc == 2:
        account2()
    elif bc == 3:
        account3()
    elif bc == 4:
        account4()
    else:
        raise RuntimeError("Fehler bei Auswahl des Bot Accounts")
    sign_up()
    time.sleep(4)

#Decline saving the password
def NoPasswordSave():
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "yWX7d"))).click()
    time.sleep(0.5)

#Don't accept notifications
def NoNotifications():
    WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, "HoLwm"))).click()
    time.sleep(0.5)

#searches for targetted account
def SearchAccount(target_account):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[placeholder="Suchen"]'))).send_keys(target_account)
    time.sleep(1)

#clicks on first suggested account
def ClickOnAccount():
    click_on_account = driver.find_element_by_class_name("-qQT3")
    click_on_account.click()
    time.sleep(2)

#clicks on the latest picture on this account
def ClickThroughPictures(target_account,bot_account):
    try:
        select_picture = driver.find_element_by_class_name("eLAPa")
        #print(select_picture)
    except:
        print("You are not following this account!")
        select_picture = None
        #print(select_picture)
        pass

    if select_picture != None:
        select_picture.click()
    else:
        driver.find_element_by_class_name("y3zKF").click()
        time.sleep(1)
        driver.quit()
        sys.exit("Sent request! \nShutting down")
    time.sleep(1)

    #Likes the post if not already done
    readOutFile(target_account,bot_account)

def EndProgram():
    driver.quit()
