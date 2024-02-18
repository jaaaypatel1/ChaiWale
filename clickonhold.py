import pyautogui
import time

last_click_x, last_click_y = pyautogui.position()

start_time = time.time()

while True:
    current_x, current_y = pyautogui.position()
    distance = ((current_x - last_click_x) ** 2 + (current_y - last_click_y) ** 2) ** 0.5  # Euclidean distance

    if distance <= 100:  # Check if within 100 pixels of last click position
        if time.time() - start_time >= 2:
            pyautogui.click()
            start_time = time.time()
    else:
        last_click_x, last_click_y = current_x, current_y
        start_time = time.time()

    # Check every 0.1 second
    time.sleep(0.1)
