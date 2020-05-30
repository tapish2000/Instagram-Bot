from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login_direct(self):
        driver = self.driver()
        driver.get("https://www.instagram.com/")
        alert = driver.switch_to.alert
        alert.dismiss()
        
        xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

        user_name_elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        pass_word_elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        pass_word_elem.clear()
        pass_word_elem.send_keys(self.password)
        pass_word_elem.send_keys(Keys.RETURN)

    def login_fb(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        alert = driver.switch_to.alert
        alert.dismiss()

        xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

        login_button = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
        login_button.click()
    
        xpath = "//*[@id='loginbutton']"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

        user_name_elem = driver.find_element_by_xpath("//input[@name='email']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        pass_word_elem = driver.find_element_by_xpath("//input[@name='pass']")
        pass_word_elem.clear()
        pass_word_elem.send_keys(self.password)
        pass_word_elem.send_keys(Keys.RETURN)

        try:
            xpath = "/html/body/div[4]/div/div/div[3]/button[2]"
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            no_notify = driver.find_element_by_xpath(xpath)
            no_notify.click()
        except:
            xpath = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img"    
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath)))  

    def profile(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")

        profile_button = driver.find_element_by_xpath("//a[@href='/tapish_1100/']")
        profile_button.click()        

    def get_following(self):
        driver = self.driver
        driver.get("https://www.instagram.com/tapish_1100/")

        xpath = "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a"    
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))) 

        following_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        following_button.click()

        xpath = "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        
        elem_in_popup = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        for i in range(55):
            elem_in_popup.send_keys(Keys.END)
            time.sleep(1)
            
        xpath = "//a[@class='FPmhX notranslate  _0imsa ']"
        following_elems = driver.find_elements_by_xpath(xpath)
        file = open("following.txt", 'w')
        lst = []
        for username in following_elems:
            lst.append(username.text)
        
        file.write(str(lst))
        
    def get_followers(self):
        driver = self.driver
        driver.get("https://www.instagram.com/tapish_1100/")
        time.sleep(2)

        following_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        following_button.click()
        time.sleep(6)

        xpath = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        
        elem_in_popup = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        for i in range(55):
            elem_in_popup.send_keys(Keys.END)
            time.sleep(1)
            
        xpath = "//a[@class='FPmhX notranslate  _0imsa ']"
        followers_elems = driver.find_elements_by_xpath(xpath)
        file = open("followers.txt", 'w')
        lst = []
        for username in followers_elems:
            lst.append(username.text)
        
        file.write(str(lst))
        
    def close_window(self):
        driver = self.driver
        driver.quit()


Insta_username = str(input("Enter your username: "))
Insta_password = str(input("Enter your password: "))
fb_login = str(input("If you have logged into Instagram using Facebook, enter 'y' otherwise 'n'."))
TapishInsta = InstaBot(Insta_username, Insta_password)
if(fb_login == 'y'):
    TapishInsta.login_fb()
elif(fb_login == 'n'):
    TapishInsta.login_direct()
else:
    print("Enter a valid option!!!")

TapishInsta.profile()
TapishInsta.get_following()
TapishInsta.get_followers()
TapishInsta.close_window()