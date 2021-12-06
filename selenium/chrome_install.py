
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())  
time.sleep(5)
driver.get("https://auth.geeksforgeeks.org/")
time.sleep(5)