import pyautogui
from time import sleep
import random

def randomWait():
  wait = round(random.uniform(0.15, 1.85), 2)
  sleep(wait)
  print('wait:' + str(wait))

def take_screenshot():
  img = pyautogui.screenshot()
  img.save('hi_test.png')

def input_hallo():
  screenWidth, screenHeight = pyautogui.size()
  currentMouseX, currentMouseY = pyautogui.position()
  pyautogui.moveTo(100, 150)
  pyautogui.click()
  pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
  pyautogui.doubleClick()
  pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
  pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
  pyautogui.press('esc')
  pyautogui.keyDown('shift')
  pyautogui.typewrite(['left', 'left', 'left', 'left', 'left', 'left'])
  pyautogui.keyUp('shift')
  pyautogui.hotkey('ctrl', 'c')
  print(screenHeight)
  print(currentMouseY)

def test():
  print('Interest Calculator:')

  amount = float(input('Principal amount ?'))
  roi = float(input('Rate of Interest ?'))
  yrs = int(input('Duration (no. of years) ?'))

  total = (amount * pow(1 + (roi/100), yrs))
  interest = total - amount
  print('\nInterest = %0.2f' %interest)