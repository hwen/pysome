import pyautogui
import random
from time import sleep
from utils import randomWait

def goBookMark():
  print('waiting...')
  sleep(3)
  print('go bookmark')
  pos = pyautogui.locateCenterOnScreen('./vscode.png')
  print(pos)
  if (pos == None):
    print('can not find image on screen')
  else:
    pyautogui.click(pos)

def goBing():
  print('waiting...')
  sleep(3)
  print('go bing...')
  pyautogui.hotkey('ctrlleft', 'l')
  bing = 'https://cn.bing.com/'
  baidu = 'https://www.baidu.com/'
  pyautogui.typewrite(baidu, interval=0.15)
  for i in range(len(baidu)):
    pyautogui.press('backspace')
  pyautogui.typewrite(bing, interval=0.1)
  pyautogui.press('enter')

def test():
  print('waiting')
  sleep(6)
  move(['left', 'left', 'top', 'right', 'right', 'bottom'])
  print('moving')

def move(keymaps):
  for key in keymaps:
    print('press:' + key)
    pyautogui.press(key)
    sleep(1)

# goBing()
# goBookMark()