
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import numpy as np
import threading
import pyautogui

width, height= pyautogui.size()
display_w = (width-40)/4



# create instance of Chrome webdriver
# driver = webdriver.Chrome(ChromeDriverManager().install())  
# time.sleep(5)
# driver.get("https://auth.geeksforgeeks.org/")
# time.sleep(5)

def runtest(l):
    print("running thread: ", l)
    # time.sleep(1)
    keyword = chunks[l][0]
    Options = webdriver.ChromeOptions()
    Options.add_argument("--app=https://youtube.com")
    # driver = webdriver.Chrome(ChromeDriverManager().install())  
    driver = webdriver.Chrome(options=Options)
    x = l*display_w
    y = 10
    driver.set_window_rect(x,y,display_w,600)
    driver.get(f'https://www.youtube.com/results?search_query={keyword}')
    for i in range(100):
        time.sleep(1)
        driver.execute_script(f'window.scrollTo(0,{str(i)}00)')
    time.sleep(10)

soluong = 4
data = open('test.txt').readlines()
chunks = np.array_split(data, int(soluong))
thread = []

for i in range(soluong):
    thread += [threading.Thread(target=runtest, args={i},)]
for t in thread:
    t.start()
for t in thread:
    t.join()

print("_________DONE____________")
