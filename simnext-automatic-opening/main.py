import pyautogui as pag
import time

#Variaveis de ambiente
initTime = 10
profileTime = 10

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
    x1, y1 = pag.locateCenterOnScreen('images/visualizacao.png')
    pag.doubleClick(x1, y1)
    print("Visualization tab open.")
    time.sleep(20)
except FileNotFoundError:
    print("Visualization button was not found.")
    flagAction = False

#Abertura do perfil de visualizacao
try:
    x2, y2 = pag.locateCenterOnScreen('images/botao-perfil.png')
    pag.doubleClick(x2, y2)
    print("Visualization profile open.")
    time.sleep(profileTime)
except:
    print("Profile button was not found.")
    flagAction = False

#Ativando tela cheia
if flagAction:
    pag.rightClick(width/2, height/2)
    pag.rightClick(width/2 + 50, height/2)
    print("Opening fullscreen...")
    time.sleep(2)
    x3, y3 = pag.locateCenterOnScreen('images/tela-cheia.png')
    pag.click(x3, y3)
else:
    print("Without fullscreen activation.")
