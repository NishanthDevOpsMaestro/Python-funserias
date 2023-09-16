import time
import pyautogui
f = open('spam.txt')

for line in f:
    pyautogui.typewrite(line)
    pyautogui.press('enter')