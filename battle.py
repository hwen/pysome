import pyautogui
import random
from time import sleep
from utils import randomWait

rpath = './resource/'
drg = './resource/dragon.png'
drgNotGood = './resource/dragon_notgood.png'
drgGood = './resource/dragon_good.png'
drgOk = './resource/dragon_ok.png'

eq = './resource/eq.png'
eqGood = './resource/eq_good.png'
eqNotGood = './resource/eq_notgood.png'
eqOk = './resource/eq_ok.png'
eqNoUse = './resource/eq_nouse.png'

elecMove = './resource/charge.png'
mushroom = './resource/mroom.png'
sweetSmell = './resource/sweetsmell.png'

battleImg = './resource/battle.png'
battleImg2 = './resource/battle2.png'
runImg = './resource/run.png'
battleFlag = './resource/battle_flag.png'

testImg = './resource/battle2.png'

def isBattleStart():
  # 识别战斗是否开始。
  pos = pyautogui.locateCenterOnScreen(battleImg, grayscale = True)
  pos2 = pyautogui.locateCenterOnScreen(battleImg2, grayscale = True)
  print('isBattleStart: ' + str(pos) + ', ' + str(pos2))
  return (pos != None or pos2 != None)

def isWildBattle():
  # 识别是否时草丛战
  pos = pyautogui.locateCenterOnScreen(battleImg, grayscale = True)
  return pos != None

def isHumanBattle():
  # 识别是否与人对战
  pos = pyautogui.locateCenterOnScreen(battleImg, grayscale = True)
  return pos != None

def isBattleEnd():
  # 识别战斗是否结束
  pos = pyautogui.locateCenterOnScreen(battleFlag, grayscale = True)
  print('isBattleEnd: ' + str(pos))
  return pos == None

def isShiny():
  # 是否是闪光
  pos = pyautogui.locateCenterOnScreen(battleImg, grayscale = True)
  return pos != None

def autoBattle():
  # 选择有效的技能。避免无效技能。
  print('battling...')

def runAway():
  pos = pyautogui.locateCenterOnScreen(runImg, grayscale = True)
  pyautogui.click(pos)
  print('run away')

def suspendBattle():
  print('suspended...')

def isOkDragonClaw():
  pos = pyautogui.locateCenterOnScreen(drgOk, grayscale = True)
  return pos != None

def isNotGoodDragonClaw():
  pos = pyautogui.locateCenterOnScreen(drgNotGood, grayscale = True)
  return pos != None 

def isGoodDragonClaw():
  pos = pyautogui.locateCenterOnScreen(drgGood, grayscale = True)
  return pos != None

def isNoUseEarthquake():
  pos = pyautogui.locateCenterOnScreen(eqNoUse, grayscale = True)
  return pos != None

def isNotGoodEarthquake():
  pos = pyautogui.locateCenterOnScreen(eqNotGood, grayscale = True)
  return pos != None

def isOkEarthquake():
  pos = pyautogui.locateCenterOnScreen(eqOk, grayscale = True)
  return pos != None

def isGoodEarthquake():
  pos = pyautogui.locateCenterOnScreen(eqGood, grayscale = True)
  return pos != None

def getDragonClawValue():
  # ok 的情况最多，放第一可以减少不必要的检测
  if isOkDragonClaw():
    return 2
  if isNotGoodDragonClaw():
    return 1
  if isGoodDragonClaw():
    return 3

def getEarthquakeValue():
  # ok 的情况最多，放第一可以减少不必要的检测
  if isOkEarthquake():
    return 2
  if isNoUseEarthquake():
    return 0
  if isNotGoodEarthquake():
    return 1
  if isGoodEarthquake():
    return 3

def useDragonClaw():
  pos = pyautogui.locateCenterOnScreen(drg, grayscale = True)
  pyautogui.click(pos)
  print('used dragon claw...')

def useEarthquake():
  pos = pyautogui.locateCenterOnScreen(eq, grayscale = True)
  pyautogui.click(pos)
  print('used earthquake...')

# 判断是否打倒一个
def isFailOne():
  print('fail one')
  return True

# 判断是否是允许出招的环境，是否网络延迟或倒下对话还没完成
def isOkToMove():
  pos = pyautogui.locateCenterOnScreen(battleImg, grayscale = True)
  if pos != None:
    print('ok to move')
    return True
  else:
    print('not ok to move')
    return False

def autoUseMove():
  if isOkToMove():
    # 使用优先级较高的
    if getDragonClawValue() >= getEarthquakeValue():
      useDragonClaw()
    else:
      useEarthquake()

# 假定已经进入正式的战斗环境
def battleForMoney():
  while True:
    autoUseMove()
    # 等待出招和损伤计算
    sleep(5)
    pyautogui.press('b')
    if isBattleEnd():
      # 读完战斗结束后的会话
      for i in range(8):
        pyautogui.press('b')
        randomWait()
      break

def useSweetSmell():
  mushroomPos = (2016, 929)
  pyautogui.click(mushroomPos)
  sleep(2)
  print('get sweet move pos...')
  # sweetSmellPos = pyautogui.locateCenterOnScreen(sweetSmell, grayscale = True)
  sweetSmellPos = (1915, 1029)
  print(sweetSmellPos)
  pyautogui.click(sweetSmellPos)
  pyautogui.press('k')
  randomWait()
  pyautogui.press('k')
  print('use sweet smell...')

def isOkToUseSweetSmell():
  sleep(1)
  return isBattleStart() == False

def battleForEv():
  smellCount = 0
  print('current smell count: ' + str(smellCount))
  while True:
    if isBattleStart():
      print('battle ready to start...')
      useEarthquake()
      randomWait()
      pyautogui.press('j')
      print('waiting...')
      sleep(3)
      print('next...')
      if smellCount > 5:
        print('smell count end...')
        break
    else:
      print('ready to use smell...')
      useSweetSmell()
      smellCount += 1
      print('waiting...')
      sleep(3)
      print('smell end...')
    
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

def useCoinMove():
  print('fuck you')

def miaomiao():
  RunCount = 0
  shinyMove()
  while RunCount < 32:
    if isBattleStart():
      RunCount += 1
      useCoinMove()
      sleep(1)
      pyautogui.press('k')
      randomWait()
      pyautogui.press('k')
    else:
      shinyMove()


def testPos():
  print('testing...')
  count = 0
  while True:
    pos = pyautogui.position()
    count += 1
    print(pos)
    if count > 40:
      break
  print('end')

def test():
  print('test...')
  x, y, z, j = pyautogui.locateOnScreen('./resource/mroom.png', grayscale = False, confidence=0.8)
  pos = (x, y)
  print(pos)
  pyautogui.moveTo(pos)

print('waiting...')
sleep(3)
print('ready to go')
# testPos()
# battleForEv()
test()