
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import numpy as np
import threading
import pyautogui
import multiprocessing


width, height= pyautogui.size()
display_w = (width-40)/4

# create instance of Chrome webdriver
# driver = webdriver.Chrome(ChromeDriverManager().install())  
# time.sleep(5)
# driver.get("https://auth.geeksforgeeks.org/")
# time.sleep(5)

def run_key(idx, key):
    keyword = key[idx][0]
    print(f"running key word: {keyword}")

    Options = webdriver.ChromeOptions()
    Options.add_argument("--app=https://youtube.com")
    # driver = webdriver.Chrome(ChromeDriverManager().install())  
    driver = webdriver.Chrome(options=Options)
    x = idx*display_w
    y = 10
    driver.set_window_rect(x,y,display_w,600)
    driver.get(f'https://www.youtube.com/results?search_query={keyword}')
    for i in range(15):
        time.sleep(1)
        driver.execute_script(f'window.scrollTo(0,{str(i)}00)')
    time.sleep(10)


# 
threads = []
threads_number = multiprocessing.cpu_count()
key_word = open('key_word.txt').readlines()
data = np.array_split(key_word, int(threads_number))

while len(data) > 0:
    key = data[:threads_number]
    print(key)
    for thread in range(threads_number):
        threads += [threading.Thread(target=run_key, args=(thread, key),)]
    data = data[threads_number:]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("_________DONE____________")
