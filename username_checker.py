import pyautogui

with open('usernames.txt', "r") as f:
username_list = f.read().splitlines()

pyautogui.write(username_list)
