import pyautogui
import time
time.sleep(5)
# print(pyautogui.size())
# time.sleep(2)
# print(pyautogui.position())
# pyautogui.moveTo(100,200,5)
# time.sleep(5)
# pyautogui.moveRel(200,500,7)
# pyautogui.scroll(-200)
# pyautogui.scroll(200)
# pyautogui.click(200,200,1,3,button="left")
distance  = 300
while distance > 0:
    pyautogui.dragRel(distance,0,1,button="left")
    distance = distance - 20
    pyautogui.dragRel(0,distance,1,button="left")
    pyautogui.dragRel(-distance,0,1,button="left")
    distance = distance - 20
    pyautogui.dragRel(0,-distance,1,button="left")
    time.sleep(2)