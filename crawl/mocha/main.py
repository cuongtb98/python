from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from setting import info

class Mocha():
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) 

    def login(self):
        driver =  self.driver
        time.sleep(2)
        driver.get("http://video.mocha.com.vn/login")
        time.sleep(5)
        txtUserID = driver.find_element_by_css_selector('#txtUserID')
        txtUserID.send_keys(self.user)
        time.sleep(2)
        txtPass = driver.find_element_by_css_selector('#txtPass')
        txtPass.send_keys(self.password)
        txtPass.send_keys(Keys.ENTER)
        time.sleep(2)
        
    def post_video(self):
        driver =  self.driver
        driver.get("http://video.mocha.com.vn/uploadvideo")
        time.sleep(5)
        dropUp = driver.find_element_by_css_selector('#dropUp')
        dropUp.click()
        time.sleep(5)
        
Mocha = Mocha(info['user'], info['password'])
Mocha.login()
Mocha.post_video()