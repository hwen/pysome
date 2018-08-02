import pyautogui
import time

def goBookMark():
  print('waiting...')
  time.sleep(3)
  print('go bookmark')
  pos = pyautogui.locateCenterOnScreen('./vscode.png')
  print(pos)
  if (pos == None):
    print('can not find image on screen')
  else:
    pyautogui.click(pos)

def goBing():
  print('waiting...')
  time.sleep(3)
  print('go bing...')
  pyautogui.hotkey('ctrlleft', 'l')
  pyautogui.typewrite('https://cn.bing.com/', interval=0.25)
  pyautogui.press('enter')


# goBing()
goBookMark()