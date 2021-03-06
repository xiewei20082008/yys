#coding=utf8
from toolkit import *
from UnionRush import UnionRush
from time import sleep
import os
import math
import sys
import time


map2 = {1:(2,10),5:(2,10),11:(2,10),4:(3,11),2:(3,11),10:(2,5),16:(3,30)}

class ExpElf:
    def __init__(self,dm,account,fb,aimEnergy,isRush = False,isDelayRush = False,shenLe = True,script= None):
        self.dm = dm
        self.moved = False
        self.fb = fb
        self.windowName = account
        self.monsterNum = map2[fb][0]
        self.movePara = map2[fb][1]
        self.gameOver = False
        self.needRecord = True
        self.shenLe = shenLe
        self.aimEnergy = aimEnergy
        self.isRush = isRush
        self.script = script
        self.nowEnergy = 0
        print 'test'
        moveWindowAndBind(self.dm,self.windowName)
        self.fan = Fan(dm,account)

        os.system('title '+'.'.join(account))

        if isDelayRush:
            self.lastRushTime = time.time()
        else:
            self.lastRushTime = 0
    def setScriptAlive(self):
        if self.script:
            self.script.mutex.acquire()
            self.script.lastAliveTime = time.time()
            self.script.mutex.release()

    def resetFB(self):
        self.moved = False
        self.monsterNum = map2[self.fb][0]

    def main(self):
        def stopConf(windowName):
            try:
                f = open('c:/anjianScript/'+windowName+'.txt','r')
                s = f.readline()
                print s
                state,chapter,aimEnergy,isRush = s.split(' ')
                state = "0"
                ss = ' '.join([state,chapter,aimEnergy,isRush])
                f.close()
                f = open('c:/anjianScript/'+windowName+'.txt','w+')
                f.write(ss)
                f.close()
                print 'end'
                return True
            except Exception as e:
                print e
                return False

        dm = self.dm
        fan = self.fan
        ret = autoBattle(dm,self,shenLe = self.shenLe,isRecordLevel = True,windowName = self.windowName,isChangeFood = True)
        if ret ==0:
            self.fullRecogTimes +=1
            if self.fullRecogTimes>4:
                stopConf(self.windowName)
                self.gameOver = True
            return 1
        if ret == 2:
            self.fullRecogTimes = 0
            return 1

        self.fullRecogTimes = 0

        intX,intY = FindPic(dm,223,525,320,601,(u"C:/anjianScript/通用经验/起始页.bmp"
            u"|C:/anjianScript/通用经验/起始页1.bmp|C:/anjianScript/通用经验/起始页2.bmp"),"000000",0.9,0)
        if intX > 0 and intY > 0:
            self.resetFB()
            print 'time diff is '+ str(time.time() - self.lastRushTime)
            if self.isRush and time.time() - self.lastRushTime > 600:
                print 'start rush'
                fan.leftclick(intX,intY)
                sleep(.500)
                ur = UnionRush(dm,self.windowName)
                ur.runUp()
                self.lastRushTime = time.time()
                print 'end rush'
                return
            ret = dm.ocr(600,11,631,25,"e4ddca-505050", 0.8)
            print ret
            # if ret.isdigit() and int(ret)>self.aimEnergy:
            #     print 'start fb'
            #     dm.moveto(390, 305)
            #     dm.leftclick()
            #     sleep(.500)
            print ret
            if ret.isdigit():
                if int(ret) != self.nowEnergy:
                    self.nowEnergy = int(ret)
                    self.setScriptAlive()
                if int(ret)>self.aimEnergy:
                    print 'start fb'
                    fan.leftclick(390, 300)
                    sleep(.500)

        intX,intY = FindPic(dm,534, 366,653, 441,u"C:/anjianScript/通用经验/探索页.bmp","000000",0.7,0)
        if intX > 0 and intY > 0:
            print 'find tansuo'

            hardX,hardY = FindPic(dm,280,200,311,219,u"C:/anjianScript/通用经验/hard.bmp","080808",0.9,0)
            if hardX > 0:
                print 'find hard'
                fan.leftclick(hardX, hardY)
                sleep(.500)

            fan.leftclick(intX, intY)
            sleep(.500)
        intX,intY = FindPic(dm,459, 316,507, 336,u"C:/anjianScript/通用经验/退出确认.bmp","000000",0.9,0)
        if intX > 0 and intY > 0:
            fan.leftclick(intX,intY)
            sleep(.500)
        intX,intY = FindPic(dm,644, 544,749, 568,u"C:/anjianScript/通用经验/战斗大场景.bmp","000000",0.6,0)
        if intX > 0 and intY > 0:
            print 'found battle map'
            if self.needRecord:
                logEnergy(dm,self,self.windowName)
                self.needRecord = False
            if not self.moved:
                moveScreen(dm,self.movePara)
                self.moved = True
                sleep(1)
            elif self.monsterNum == 0:
                fan.leftclick(29, 39)
                sleep(.500)
            else:
                ret = self.chooseMonster()
                if ret == 1:
                    self.monsterNum = self.monsterNum-1
                else:
                    self.monsterNum = 0

        intX,intY = FindPic(dm,300,50,460,150,u"C:/anjianScript/通用经验/顶部结界突破.bmp|C:/anjianScript/通用经验/顶部结界突破1.bmp","050505",0.8,0)
        if intX > 0 and intY > 0:
            fan.leftclick(63,566)
            sleep(1.0)

    def chooseMonster(self):
        dm = self.dm
        fan = self.fan
        if self.monsterNum == 0:
            return 0
        times = 30
        for i in range (0,times):
            bishouString = dm.FindPicEx(0, 102, 802, 554, u"C:/anjianScript/通用经验/匕首.bmp", "000000", 0.6, 0)
            if len(bishouString) > 0:
                bishou = bishouString.split('|')
                if len(bishou) != self.monsterNum:
                    print 'monster not enough'
                    sleep(.100)
                    continue
            else:
                print 'no bi shou'
                sleep(.100)
                continue
            # expString = dm.FindStr(0, 102, 802, 554, "经验怪2|经验怪1", "e0d0a6-101010|6b1911-101010", 0.6,intX,intY)
            # TracePrint expString
            dm.SetPath(u"c:/anjianScript/通用经验")
            expString = dm.FindPicExS(0, 102, 802, 554,r"exp1.bmp|exp2.bmp|exp3.bmp|exp4.bmp|exp5.bmp|exp6.bmp|exp7.bmp|exp8.bmp|exp9.bmp|exp10.bmp|exp11.bmp|exp12.bmp|exp13.bmp|exp14.bmp|exp15.bmp|exp16.bmp|exp17.bmp","101010",0.75,0)
            # expString = dm.FindStrExS(0, 102, 802, 554, "经验怪4|经验怪3|经验怪2|经验怪1", "e0d0a6-101010|6b1911-101010", 0.7)
            # print expString
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
    def runUp(self):
        while not self.gameOver:
            self.main()
            sleep(1)
        sendToServer('elf thread end!(full)')
        print 'elf thread end!'

def calDistance(a,b,c,d):
    return (abs(c-a)**2 + abs(d-b)**2)**0.5

def moveScreen(dm,movePara):
    # dm_ret = dm.CaptureJpg(0,0,300,300,"e:/screen.jpg",50)
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
