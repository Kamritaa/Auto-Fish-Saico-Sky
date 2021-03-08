from pyautogui import * 
import pyautogui
import time 
import keyboard 
import random
import win32api, win32con

time.sleep(2)

time2 = 0

print(time2)

#def click(x,y):
#    win32api.SetCursorPos((x,y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
#    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

while 1:
    if pyautogui.locateOnScreen('fish3.png', confidence=0.4) != None:
        time2 = 0
        print("I can see it")
        time.sleep(0.5)
        #click(0,0)
        pyautogui.click(button='right')
        print("Clicked")
        
    else:
        print("I am unable to see it")
        time.sleep(0.5)
        time2 = time2 + 1
        print(time2)
        if time2 > 40:
            pyautogui.click(button='right')
            time.sleep(0.5)
            pyautogui.click(button='right')
            print("Clicked to reset")
            time2 = 0
            
