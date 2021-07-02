#pip install pyautogui first
import pyautogui, time
time.sleep(5)
f=open("cursed.txt",'r')
for die in f:
    pyautogui.typewrite(die)
    pyautogui.press("enter")
