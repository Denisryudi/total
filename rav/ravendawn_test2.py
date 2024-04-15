import pyautogui
import subprocess
import time
from dotenv import load_dotenv
import os

pyautogui.FAILSAFE = True
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa a variável de ambiente CHAVE_DIRETORIO
link = os.getenv('CHAVE_DIRETORIO')

def encontrar_imagem(imagem):
    while not pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9):  # reconhecimento
        time.sleep(1)
        encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    return encontrou


#abrir rav #r = diz para nao procurar caracteres especiais
# subprocess.Popen([fr"{link}"])

# encontrou = encontrar_imagem("raven_image.png")
#rav aberto

# #world
# encontrou = encontrar_imagem("anger.PNG")
# pyautogui.click(pyautogui.center(encontrou))
#
# # #auth
# encontrou = encontrar_imagem("auth.PNG")
# pyautogui.click(pyautogui.center(encontrou))
# time.sleep(20)
# #
# # #login
# encontrou = encontrar_imagem("login.PNG")
#
# pyautogui.click(pyautogui.center(encontrou))
#encontrou = encontrar_imagem("enter.PNG")
# #enter character

# #market
# time.sleep(2)
# pyautogui.press('f')
# time.sleep(5)
# encontrou_market = pyautogui.locateOnScreen("market.PNG", grayscale=True, confidence=0.9)
#
# pyautogui.click(pyautogui.center(encontrou_market))
#
# #coal
# time.sleep(2)
#
# #valores
# encontrou_valores = pyautogui.locateOnScreen("113.PNG", grayscale=True, confidence=0.9)
#
# pyautogui.click(pyautogui.center(encontrou_valores))
#
# encontrou_buy = pyautogui.locateOnScreen("buy.PNG", grayscale=True, confidence=0.9)
# time.sleep(1)
# pyautogui.click(pyautogui.center(encontrou_buy))

