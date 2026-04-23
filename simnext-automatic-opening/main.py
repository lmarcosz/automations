import os
import sys
import time
import pyautogui as pag

def resourcePath(imagePath):
    try:
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")
    
    return os.path.join(basePath, imagePath)


#Variaveis de ambiente
initTime = 4
profileTime = 5

#Aguardando o computador inicializar
print("==========================")
print("SIM NEXT AUTOMATIC OPENING")
print("==========================")
while(initTime > 0):
    print(f'Waiting Windows complete initialization... {initTime}s{" "*10}', end="\r")
    time.sleep(1)
    initTime -= 1
print("\n")

#Obtendo resolucao da tela
width, height = pag.size()
flagAction = True

#Abertura da aba visualizacao
try:
    imagePath1 = resourcePath(os.path.join('images', 'visualizacao.png'))
    x1, y1 = pag.locateCenterOnScreen(imagePath1, confidence=0.9)
    pag.doubleClick(x1, y1)
    print("Visualization tab open.")
    time.sleep(20)
except Exception as e:
    print(f"Visualization button was not found {e}.")
    flagAction = False

#Abertura do perfil de visualizacao
try:
    imagePath2 = resourcePath(os.path.join('images', 'botao-perfil.png'))
    x2, y2 = pag.locateCenterOnScreen(imagePath2, confidence=0.9)
    pag.doubleClick(x2, y2)
    print("Visualization profile open.")
    time.sleep(profileTime)
except Exception:
    print(f"Profile button was not found {e}.")
    flagAction = False

#Ativando tela cheia
if flagAction:
    pag.rightClick(width/2, height/2)
    pag.rightClick(width/2 + 50, height/2)
    print("Opening fullscreen...")
    time.sleep(2)
    try:
        imagePath3 = resourcePath(os.path.join('images','tela-cheia.png'))
        x3, y3 = pag.locateCenterOnScreen(imagePath3, confidence=0.9)
        pag.click(x3, y3)
    except Exception as e:
        print(f"Fullscreen button was not found {e}.")
else:
    print("Without fullscreen activation.")
