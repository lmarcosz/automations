import pyautogui as pag
import time

#Aguardando o computador inicializar
#time.sleep(180)
time.sleep(2)

#Obtendo resolucao da tela
width, height = pag.size()
flagAction = True

#Abertura da aba visualizacao
try:
    x1, y1 = pag.locateCenterOnScreen('images/visualizacao.png')
    pag.doubleClick(x1, y1)
    print("Aba de visualizacao aberta.")
    time.sleep(20)
except FileNotFoundError:
    print("Visualization button not found.")
    flagAction = False

#Abertura do perfil de visualizacao
try:
    x2, y2 = pag.locateCenterOnScreen('images/botao-perfil.png')
    pag.doubleClick(x2, y2)
    print("Perfil de visualizacao aberto.")
    time.sleep(60)
except:
    print("Profile button not found.")
    flagAction = False

#Ativando tela cheia
if flagAction:
    pag.rightClick(width/2, height/2)
    pag.rightClick(width/2 + 50, height/2)
    time.sleep(1)
    x3, y3 = pag.locateCenterOnScreen('images/tela-cheia.png')
    pag.click(x3, y3)
else:
    print("Without fullscreen activation.")

