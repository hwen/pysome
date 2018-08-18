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

"""
不知为什么么，pyautogui 在游戏的时候图像识别率很低。(但chrome那个测试，却是很灵)
试了下AutoIt3的原生脚本，还有按键精灵，同样有识别率问题。
而且在普通屏下测试了也是不行，又试过换过游戏UI，希望提高识别率。
图像识别还是不行。
搞到2点多。。。还是放弃这个方案算了。
嘛，算是学到不少东西。
py 还有个叫 pywinauto 也是个不错的库。以后如果要写自动脚本，可以试试。

Nodejs 那边就有点搞笑了。。。
有个叫 Robotjs 的东东，库都写了两年多了，图像识别还放在项目 planning 里
笑人。。。
"""


mushroom = './resource/mushroom.bmp'
sweetSmell = './resource/sweetsmell.bmp'

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

def test():
  # 安装 opencv 后可以加 confidence
  pos = pyautogui.locateCenterOnScreen(mushroom, grayscale = True, confidence = 0.8)
  pos2 = pyautogui.locateCenterOnScreen(sweetSmell)
  print('mushroom is:')
  print(pos)
  print('sweetSmell is:')
  print(pos2)

print('waiting...')
sleep(5)
print('ready....')
test()