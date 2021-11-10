import webbrowser
import pyautogui
import time 
url = 'https://colab.research.google.com/drive/1z0tInSw1wTHlP8WltiJ8OGEvDuiyhtP2'
url1 = 'https://colab.research.google.com/drive/1wrFf_qZlqQPI9ED2lqF5A6Q49hqSD6Np'
url2 = 'https://colab.research.google.com/drive/19NGWkjkTmPSNkptc0sTY0vN3rQRBIXPe'

webbrowser.register('firefox',
 None,
 webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
webbrowser.get('firefox').open(url)
time.sleep(10)

pyautogui.keyDown('Ctrl')
pyautogui.press('F9')
pyautogui.keyUp('Ctrl')
time.sleep(2)

pyautogui.keyDown('Ctrl')
pyautogui.press('F1')
pyautogui.keyUp('Ctrl')

time.sleep(2)
pyautogui.press('Space')
time.sleep(2)
pyautogui.keyDown('Ctrl')
pyautogui.press('F9')
pyautogui.keyUp('Ctrl')
time.sleep(2)

webbrowser.register('firefox',
 None,
 webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
webbrowser.get('firefox').open(url1)
time.sleep(10)
pyautogui.keyDown('Ctrl')
pyautogui.press('F9')
pyautogui.keyUp('Ctrl')
time.sleep(1)

pyautogui.keyDown('Ctrl')
pyautogui.press('F1')
pyautogui.keyUp('Ctrl')

time.sleep(2)
pyautogui.press('Space')
time.sleep(2)
pyautogui.keyDown('Ctrl')
pyautogui.press('F9')
pyautogui.keyUp('Ctrl')
time.sleep(2)

webbrowser.register('firefox',
 None,
 awebbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
webbrowser.get('firefox').open(url2)
time.sleep(10)
pyautogui.keyDown('Ctrl')
pyautogui.press('F9')
pyautogui.keyUp('Ctrl')
time.sleep(2)

pyautogui.keyDown('Ctrl')
pyautogui.press('F1')
pyautogui.keyUp('Ctrl')

time.sleep(2)
pyautogui.press('Space')
time.sleep(2)
pyautogui.keyDown('Ctrl')
pyautogui.press('F9')
pyautogui.keyUp('Ctrl')