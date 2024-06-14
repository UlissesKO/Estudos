import pyautogui
from mouseinfo import mouseInfo
import time

pos1 = 346,956
pos2 = 480,530
pos3 = 682,529
pos4 = 874,533
pos5 = 480,594
pos6 = 681,593
pos7 = 873,590

time.sleep(2)

def tocar_coisa():
    pyautogui.leftClick(pos1)    
    for i in range(30):
        pyautogui.leftClick(pos2)
        pyautogui.leftClick(pos3)
        pyautogui.leftClick(pos4)
        pyautogui.leftClick(pos5)
        pyautogui.leftClick(pos6)
        pyautogui.leftClick(pos7)

mouseInfo()