import pyautogui
import PIL

with open('usernames.txt', "r") as f:
username_list = f.read().splitlines()

pyautogui.write(username_list)

image = pyautogui.screenshot(region=0,0, 300, 400))
