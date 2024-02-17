import pyautogui
import time


x, y = pyautogui.position()


start_time = time.time()

while True:
    
    if pyautogui.position() != (x, y):
        
        x, y = pyautogui.position()
        start_time = time.time()
    else:
        
        if time.time() - start_time >= 2:
            
            pyautogui.click()
           
            start_time = time.time()

    # Check every 0.1 second
    time.sleep(0.1)
