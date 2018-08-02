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

def isIronBird():
  return True

def isOkDragonClaw():
  return True

def isGoodDragonClaw():
  return True

def isGoodEarthquake():
  return True

def useDragonClaw():
  print('dragon claw')

def useEarthquake():
  print('earthquake')

# 判断是否打倒一个
def isFailOne():
  print('fail one')
  return True

# 判断是否是允许出招的环境，是否网络延迟或倒下对话还没完成
def isOkToMove():
  print('hi is ok to move')
  return True

def autoUseMove():
  if isOkToMove():
    # 遇到盔甲鸟或者地震没有效果绝佳且龙爪有效的情况，使用龙爪
    if isIronBird() or (isGoodEarthquake() == False and (isOkDragonClaw() or isGoodDragonClaw())):
      useDragonClaw()
    else:
      useEarthquake()

# 假定已经进入正式的战斗环境
def battleForMoney():
  while True:
    autoUseMove()
    # 等待出招和损伤计算
    sleep(5)
    if isFailOne():
      pyautogui.press('b')
      pyautogui.press('b')
      pyautogui.press('b')
    if isBattleEnd():
      # 读完战斗结束后的会话
      for i in range(8):
        randomWait()
        pyautogui.press('b')
      break

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
  while shinyRunCount < 100000:
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

