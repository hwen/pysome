import pyautogui
import random
from time import sleep
from utils import randomWait

def isBattleStart():
  # 识别战斗是否开始。
  return True

def isWildBattle():
  # 识别是否时草丛战
  return True

def isHumanBattle():
  # 识别是否与人对战
  return True

def isBattleEnd():
  # 识别战斗是否结束
  return True

def isShiny():
  # 是否是闪光
  return True

def autoBattle():
  # 选择有效的技能。避免无效技能。
  print('battling...')

def runAway():
  print('run away')

def suspendBattle():
  print('suspended...')

def shinyMove():
  pyautogui.keyDown('right')
  sleep(round(random.uniform(1.5, 1.8), 2))
  pyautogui.keyUp('right')
  pyautogui.keyDown('left')
  sleep(round(random.uniform(1.5, 1.8), 2))
  pyautogui.keyUp('left')

def findShiny():
  shinyRunCount = 0
  shinyMove()
  while True:
    if isBattleStart():
      shinyRunCount += 1
      if isShiny():
        suspendBattle()
        print('hey man!!!!shiny!!!')
        print('after running for ' + str(shinyRunCount) + ' time!!!')
      else:
        runAway()
        shinyMove()
    else:
      shinyMove()

