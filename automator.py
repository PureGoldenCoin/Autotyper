import pyautogui
import time
import random

time.sleep(5)

my_text = "Feliz Navivad"

for letter in my_text:
    pyautogui.write(letter)
    
    # Pick a random pause between 0.05 and 0.25 seconds per letter
    random_pause = random.uniform(0.05, 0.25)
    time.sleep(random_pause)
