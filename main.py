from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep, time
from datetime import datetime
import random

t = 0
delay = 5
delay_10 = 10

USERNAME = ""
PASSWORD = ""
CLASS_NAME_ADD_COMMENT = "_ablz"
URL_BASE = "https://www.instagram.com/"
URL_POST = f"{URL_BASE}p/Cfb0ZEjOSIA5A32/"

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(url=URL_BASE)

browser.delete_all_cookies()

sleep(delay)

valid = False

while not valid:
    try:
        login_link = browser.find_element(By.XPATH,"//a[text()='Log in']")
        login_link.click()
        valid = True
        print("Clicked to Log In")
    except:
        print("Waiting to Click to Log In")
        sleep(1)
        valid = False

        try:
            browser.find_element(By.CSS_SELECTOR,"input[name='username']")
            valid = True
        except:
            print()

valid = False

while not valid:
    try:
        username_input = browser.find_element(By.CSS_SELECTOR,"input[name='username']")
        password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']")

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)

        login_button = browser.find_element(By.XPATH,"//button[@type='submit']")
        login_button.click()
        valid = True 
        print("Logged")
    except:
        print("Waiting - To Log In")
        sleep(1)
        valid = False

valid = False

sleep(delay)

while not valid:
    try:
        notification = browser.find_element(By.XPATH, '//*[contains(text(), "Not Now")]')
        notification.click()

        valid = True 
        print("Not Now")
    except:
        print("Waiting - Not Now")
        sleep(1)
        valid = False

browser.get(URL_POST)

#arrays of comments
comments_array = ["@personA", "@personB", "@personC", "@personD"]

print("Starting...")
sleep(delay)

def get_comment():
    return comments_array[random.randint(0, len(comments_array) - 1)]

valid = False

while not valid:
    t+=1
    print(f"Total: {t} -> {str(datetime.fromtimestamp(int(time())))}")
    try:
        field = browser.find_element(By.CLASS_NAME, CLASS_NAME_ADD_COMMENT)
        field.click()

        field = browser.find_element(By.CLASS_NAME, CLASS_NAME_ADD_COMMENT)
        field.send_keys(get_comment())
        
        try:
            post_button = browser.find_element(By.XPATH,"//button[@type='submit']")
            post_button.click()

            sleep(delay)
            
            comment = browser.find_element(By.CLASS_NAME, CLASS_NAME_ADD_COMMENT)
            
            if len(comment.text) != 0:
                sleep(delay_10)

                post_button = browser.find_element(By.XPATH,"//button[@type='submit']")
                post_button.click()
        except:
            sleep(delay)

            # browser.find_element(By.CLASS_NAME, CLASS_NAME_ADD_COMMENT).clear()
            field = browser.find_element(By.CLASS_NAME, CLASS_NAME_ADD_COMMENT)
            field.send_keys(" ")

            t=t-1
        
        int_random = random.randint(65, 120)
        print(f" Waiting for {int_random} seconds")
        sleep(int_random)
    except NameError as err:
        sleep(delay)
        print("problem - "+err)
        valid = True
        browser.quit()

browser.quit()


     
