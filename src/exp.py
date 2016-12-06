#coding=utf8
from toolkit import *
from time import sleep
import math

dm = reg()
print dm
windowName = u"小号"
moveWindowAndBind(dm,windowName)

class controlFactor:
    def __init__(self):
        self.moved = False
        self.monsterNum = 2
        self.movePara = 10
        self.gameOver = False
        self.needRecord = True
        self.aimEnergy = 3
    def resetFB(self):
        self.moved = False
        self.monsterNum = 2
        self.movePara = 10

def calDistance(a,b,c,d):
    return (abs(c-a)**2 + abs(d-b)**2)**0.5

def moveScreen(dm,movePara):
    dm_ret = dm.CaptureJpg(0,0,300,300,"e:/screen.jpg",50)
    dm.moveto(685, 87)
    dm.leftdown()
    dm.leftdown()
    sleep(0.500)
    for i in range(0,movePara):
        dm.mover(- 50 , 0)
        sleep(.050)

    sleep(.500)
    dm.leftup()
    dm.leftup()
    sleep(.500)

def main(dm):
    intX,intY = FindPic(dm,244, 549,277, 585,u"C:/anjianScript/通用经验/起始页.bmp","000000",0.9,0)
    if intX > 0 and intY > 0:
        cf.resetFB()
        dm.moveto(390, 280)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,534, 366,653, 441,u"C:/anjianScript/通用经验/探索页.bmp","000000",0.7,0)
    if intX > 0 and intY > 0:
        dm.moveto(intX, intY)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,459, 316,507, 336,u"C:/anjianScript/通用经验/退出确认.bmp","000000",0.9,0)
    if intX > 0 and intY > 0:
        dm.moveto(intX,intY)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,644, 544,749, 568,u"C:/anjianScript/通用经验/战斗大场景.bmp","000000",0.6,0)
    if intX > 0 and intY > 0:
        print 'found battle map'
        if cf.needRecord:
            logEnergy(dm,cf,windowName)
            cf.needRecord = False
        if not cf.moved:
            moveScreen(dm,cf.movePara)
            cf.moved = True
            sleep(1)
        elif cf.monsterNum == 0:
            dm.moveto(29, 39)
            dm.leftclick()
            sleep(.500)
        else:
            ret = chooseMonster(dm)
            if ret == 1:
                cf.monsterNum = cf.monsterNum-1
            else:
                cf.monsterNum = 0
    intX,intY = FindPic(dm,227,46,385,190,u"C:/anjianScript/阴阳师碎片/胜利鼓.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        dm.moveto(307, 121)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,658, 536,798, 602,u"C:/anjianScript/阴阳师碎片/准备下棍子.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        dm.moveto(730, 498)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,290, 191,496, 395,u"C:/anjianScript/阴阳师碎片/胜利佛1.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        cf.needRecord = True
        dm.moveto(307, 121)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,350, 390,434, 449,u"C:/anjianScript/阴阳师碎片/胜利碗.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        dm.moveto(307, 121)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,290, 332,356, 356,u"C:/anjianScript/阴阳师碎片/我很忙.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        dm.moveto(intX, intY)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,401, 300,546, 392,u"C:/anjianScript/阴阳师碎片/协助.bmp","000000", 0.6, 0)
    if intX > 0 and intY > 0:
        dm.moveto(473, 346)
        dm.leftclick()
        sleep(.500)

def chooseMonster(dm):
    if cf.monsterNum == 0:
        return 0
    times = 30
    for i in range (0,times):
        bishouString = dm.FindPicEx(0, 102, 802, 554, u"C:/anjianScript/通用经验/匕首.bmp", "000000", 0.6, 0)
        if len(bishouString) > 0:
            bishou = bishouString.split('|')
            if len(bishou) != cf.monsterNum:
                print 'monster not enough'
                sleep(.100)
                continue
        else:
            sleep(.100)
            continue
        # expString = dm.FindStr(0, 102, 802, 554, "经验怪2|经验怪1", "e0d0a6-101010|6b1911-101010", 0.6,intX,intY)
        # TracePrint expString
        dm.SetPath(u"c:/anjianScript/通用经验")
        expString = dm.FindPicExS(0, 102, 802, 554,r"exp1.bmp|exp2.bmp|exp3.bmp|exp4.bmp|exp5.bmp|exp6.bmp|exp7.bmp|exp8.bmp|exp9.bmp|exp10.bmp|exp11.bmp|exp12.bmp|exp13.bmp|exp14.bmp|exp15.bmp|exp16.bmp|exp17.bmp","101010",0.75,0)
        # expString = dm.FindStrExS(0, 102, 802, 554, "经验怪4|经验怪3|经验怪2|经验怪1", "e0d0a6-101010|6b1911-101010", 0.7)
        print expString
        if len(expString) > 0:
            expPos = expString.split('|')
            for a in expPos:
                aa = a.split(',')
                # MoveTo aa(1),aa(2)
                refX = int(aa[1])
                refY = int(aa[2]) - 80
                # MoveTo refX,refY
                sortedString = dm.SortPosDistance(bishouString, 0, refX, refY)
                # TracePrint cstr(refX)+","+ cstr(refY)
                # TracePrint sortedString
                sortedPoint = sortedString.split('|')
                if len(sortedPoint) == 1:
                    s = sortedPoint[0].split(',')
                    aimX = int(s[1])
                    aimY = int(s[2])
                else:
                    s = sortedPoint[0].split(',')
                    a = int(s[1])
                    b = int(s[2])
                    s = sortedPoint[1].split(',')
                    c = int(s[1])
                    d = int(s[2])
                    if abs(a - refX) > 100 or abs(b - refY) > 140:
                        # TracePrint "不到范围值"
                        sleep(.100)
                        continue
                    diff1 = calDistance(refX, refY, a, b)
                    diff2 = calDistance(refX, refY, c, d)
                    print u"--差值"
                    print (diff1-diff2)
                    if abs(diff1- diff2)>100:
                        aimX = a
                        aimY = b
                    else:
                        # TracePrint "离的太近了，没超过两倍距离"
                        if times < 15:
                            times = 15
                        sleep(.100)
                        continue
                print u"！！！found"
                # MoveTo aimX + 5, aimY + 5
                dm.MoveTo(aimX + 5, aimY + 5)
                dm.leftclick()
                sleep(.500)
                return 1
        sleep(.100)
    print "10 seconds not found"
    return 0

cf = controlFactor()
while not cf.gameOver:
    main(dm)
    sleep(1)

# init()
# while not gameOver:
#     main()
#     sleep(1)
