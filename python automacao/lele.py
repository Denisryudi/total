import pyautogui
import subprocess
import time
from dotenv import load_dotenv
import os
import keyboard
pyautogui.FAILSAFE = True
#mouseinfo  >>> from mouseinfo import mouseInfo   -- mouseInfo()
time.sleep(2)

while True:
    encontrou_comentar = pyautogui.locateOnScreen("comentar.jpg", grayscale=True, confidence=0.9)
    time.sleep(10)
    pyautogui.click(pyautogui.center(encontrou_comentar))

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(10)
    #publicar
    encontrou_publicar = pyautogui.locateOnScreen("publicar.jpg", grayscale=True, confidence=0.9)
    time.sleep(10)
    pyautogui.click(pyautogui.center(encontrou_publicar))
    time.sleep(15)





