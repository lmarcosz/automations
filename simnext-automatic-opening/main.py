import pyautogui as pag
import time

#Aguardando o computador inicializar
#time.sleep(180)
time.sleep(5)

#Obtendo resolucao da tela
width, height = pag.size()

#Abrindo a aba visualizacao
x1, y1 = pag.locateCenterOnScreen('images/visualizacao.png')
pag.doubleClick(x1, y1)
time.sleep(20)

#Abrindo perfil de visualizacao
x2, y2 = pag.locateCenterOnScreen('images/botao-perfil.png')
pag.doubleClick(x2, y2)
time.sleep(60)

#Ativando tela cheia
#pag.rightClick(width/2, height/2)
pag.rightClick(width/2 + 50, height/2)
time.sleep(1)
x3, y3 = pag.locateCenterOnScreen('images/tela-cheia.png')
pag.click(x3, y3)
