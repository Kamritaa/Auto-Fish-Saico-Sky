#modules needed
from pyautogui import * 
import pyautogui
import time 

#delay on program start
time.sleep(2) 

#set update to 0 on start
update = 0
print(update)

#infinate while loop
while 1:
    #checks for the image using 40% confidence 
    if pyautogui.locateOnScreen('fish.png', confidence=0.4) != None:
        
        #if found update set to 0
        update = 0
        print("I can see it")
        time.sleep(0.5)
        
        #right click to reel rod
        pyautogui.click(button='right')
        print("Clicked")
        
        #due to a delay it will cast it in same if statement 
        
    else:
        
        #if not found update will increase for 20 seconds
        print("Not Visible")
        time.sleep(0.5)
        update = update + 1
        print(update)
        
        #if no fish found in 20 seconds then program will restart as plugin may have glitched 
        if update > 40:
            
            #reels and casts rod
            pyautogui.click(button='right')
            time.sleep(0.5)
            pyautogui.click(button='right')
            
            #sets update to 0
            print("Clicked to reset")
            update = 0
