import time
import pyautogui
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
pyautogui.click(1172, 1039)
time.sleep(5)
pyautogui.write('facebook.com', interval=0.25)
pyautogui.press('enter')
time.sleep(7)
pyautogui.click(969, 609)
time.sleep(10)
pyautogui.write('em nguyen hoai nam yeu anh thuan hoang pro vip', interval=0.25)
pyautogui.click(1030, 794)
