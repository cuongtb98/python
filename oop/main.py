import pyautogui
import requests
import time

while True:
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'f9')
    pyautogui.press('f12')
    time.sleep(2)
    pyautogui.write('window.location.href')
    time.sleep(2)
    pyautogui.press('enter') 
    # pyautogui.hotkey('ctrl', 'tab')