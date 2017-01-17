#coding=utf8
from toolkit import *
from time import sleep
import datetime
import time
import threading
from AutoHun10 import AutoHun10

inBattle = False

class Yuhun:
    def __init__(self,dm,windowName,times = 0,ishun10 = False):
        self.dm = dm
        self.windowName = windowName
        self.times = times
        self.add = 1
        self.nowTimes = 0
        self.fan = Fan(dm,windowName)
        self.ishun10 = ishun10
        self.afterGuiwang = False
        self.guiwangTime = 0

    def guiwangLoop(self,dm,fan = None):
        if not fan:
            fan = self.fan

        intX,intY = FindPic(dm,740,540,765,564,u"C:/anjianScript/通用经验/寻找鬼王.bmp","030303",0.9,0)
        if intX> 0 :
            if self.afterGuiwang or self.guiwangTime >4:
                self.guiwangTime = 0
                fan.leftclick(42,34) # 退出鬼王页
                sleep(2.500)

            else:
                self.guiwangTime+=1
                fan.leftclick(398,240)
                sleep(2.500)
        intX,intY = FindPic(dm,570,395,611,420,u"C:/anjianScript/通用经验/鬼王挑战.bmp","030303",0.9,0)
        if intX> 0 :
            self.guiwangTime=0
            if self.afterGuiwang:
                fan.leftclick(655,176) # 退出鬼王页
                sleep(.500)
                return

            for i in range(5):
                x,y = FindPic(dm,164,182,231,362,u"C:/anjianScript/通用经验/蓝点.bmp","030303",0.9,0)
                if x>0:
                    sleep(.500)
                    fan.leftclick(x,y)
                    sleep(1.00)
                    fan.leftclick(x,y)
                    sleep(0.50)
                    fan.leftclick(591,414)
                    sleep(.500)
                    break
                else:
                    start = (251,343)
                    end = (251,200)
                    fan.leftdown(start[0],start[1])
                    sleep(.500)
                    # fan.leftdownmove(start[0],end[1])
                    # fan.leftdownmove(end[0],end[1])
                    # sleep(1.500)
                    dragMoveTo(fan,start,(start[0],end[1]))
                    dragMoveTo(fan,(start[0],end[1]),end)
                    sleep(.300)
                    fan.leftup(start[0],end[1])
                sleep(1.5)
            else:
                self.afterGuiwang = True

        # intX,intY = FindPic(dm,475,392,713,587,u"C:/anjianScript/通用经验/详细.bmp","030303",0.9,0)
        # if intX>0:
        #     fan.leftclick(42,34)
        #     self.afterGuiwang = False
        #     sleep(.500)

        intX,intY = FindPic(dm,554,428,671,479,u"C:/anjianScript/通用经验/御魂start.bmp","030303",0.8,0)
        if intX>0 and dm.cmpColor(626,368,'737573',0.9)!=0:
            fan.leftclick(618,452)
            sleep(.500)

        intX,intY = FindPic(dm,574,440,649,458,u"C:/anjianScript/通用经验/灰开始战斗.bmp","030303",0.9,0)
        if intX>0:
            fan.leftclick(379,293)
            sleep(0.500)
            while True:
                intX,intY = FindPic(dm,460,420,503,443,u"C:/anjianScript/通用经验/邀请.bmp","030303",0.9,0)
                global inBattle
                if intX >0 and not inBattle:
                    sleep(.800)
                    fan.leftclick(314,218)
                    sleep(.500)
                    fan.leftclick(489,218)
                    sleep(.500)
                    fan.leftclick(486,435)
                    sleep(.500)
                    break

            sleep(4)

        intX,intY = FindPic(dm,700,0,750,50,u"C:/anjianScript/通用经验/邮件.bmp","000000",0.8,0)
        if intX>0:
            print 'find mail'
            # dm.moveto(249,541)
            # dm.leftclick()
            fan.leftclick(249,541)
            sleep(.500)

        intX,intY = FindPic(dm,670,455,705,490,u"C:/anjianScript/通用经验/地图.bmp","030303",0.9,0)
        if intX>0:
            fan.leftclick(intX,intY)
            self.afterGuiwang = False
            sleep(.500)

        intX,intY = FindPic(dm,335,340,377,363,u"C:/anjianScript/通用经验/无响应等待.bmp","030303",0.9,0)
        if intX>0:
            fan.leftclick(intX,intY)
            sleep(.500)

        intX,intY = FindPic(dm,465,241,525,285,u"C:/anjianScript/通用经验/无碎片.bmp","030303",0.9,0)
        if intX>0:
            fan.leftclick(655,176)
            sleep(.500)

        intX,intY = FindPic(dm,682,556,777,587,u"C:/anjianScript/公会突破/鼓下.bmp","000000",0.8,0)
        if intX>0:
            fan.leftclick(724,500)
            sleep(.800)
        intX,intY = FindPic(dm,227,46,385,190,u"C:/anjianScript/阴阳师碎片/胜利鼓.bmp","000000", 0.9, 0)
        if intX > 0 and intY > 0:
            fan.leftclick(307, 121)
            sleep(.500)
        intX,intY = FindPic(dm,290, 191,496, 395,u"C:/anjianScript/阴阳师碎片/胜利佛1.bmp","000000", 0.9, 0)
        if intX > 0 and intY > 0:
            fan.leftclick(307, 121)
            sleep(.500)
        intX,intY = FindPic(dm,350, 390,434, 449,u"C:/anjianScript/阴阳师碎片/胜利碗.bmp","000000", 0.9, 0)
        if intX > 0 and intY > 0:
            fan.leftclick(307, 121)
            sleep(.500)

    def mainLoop(self,dm,fan = None):
        if not fan:
            fan = self.fan
        if not self.ishun10:
            intX,intY = FindPic(dm,17,553,55,572,u"C:/anjianScript/通用经验/手动.bmp","000000",0.8,0)
            if intX> 0 :
                fan.leftclick(intX,intY)
                sleep(.500)
        intX,intY = FindPic(dm,554,428,671,479,u"C:/anjianScript/通用经验/御魂start.bmp","030303",0.8,0)
        if intX > 0 and intY > 0:
            fan.leftclick(intX,intY)
            sleep(.500)
        intX,intY = FindPic(dm,58,132,119,187,u"C:/anjianScript/通用经验/御魂cross.bmp","030303",0.8,0)
        if intX > 0 and intY > 0:
            sleep(0.5)
            intX,intY = FindPic(dm,58,132,119,187,u"C:/anjianScript/通用经验/御魂cross.bmp","030303",0.7,0)
            if intX > 0 and intY > 0:
                fan.leftclick(intX,intY)
                sleep(.500)
        intX,intY = FindPic(dm,682,556,777,587,u"C:/anjianScript/公会突破/鼓下.bmp","000000",0.8,0)
        if intX>0:
            global inBattle
            inBattle = True
            ah = AutoHun10(dm,self.windowName)
            fan.leftclick(724,500)
            sleep(.500)
            fan.leftclick(724,500)
            sleep(.800)
            if not self.ishun10:
                return

            while True:
                ret = ah.mainLoop()
                if ret == 0:
                    break
                sleep(.500)

            sleep(.500)
        intX,intY = FindPic(dm,227,46,385,190,u"C:/anjianScript/阴阳师碎片/胜利鼓.bmp","000000", 0.9, 0)
        if intX > 0 and intY > 0:
            self.nowTimes+= self.add
            self.add = 0
            if self.nowTimes >= self.times and self.times!=0:
                return False
            fan.leftclick(307, 121)
            sleep(.500)
        intX,intY = FindPic(dm,290, 191,496, 395,u"C:/anjianScript/阴阳师碎片/胜利佛1.bmp","000000", 0.9, 0)
        if intX > 0 and intY > 0:
            self.add = 1
            fan.leftclick(307, 121)
            sleep(.500)
        intX,intY = FindPic(dm,350, 390,434, 449,u"C:/anjianScript/阴阳师碎片/胜利碗.bmp","000000", 0.9, 0)
        if intX > 0 and intY > 0:
            global inBattle
            inBattle = False
            if self.ishun10:
                dm.Capture(0,0,800,600,"c:/bonus/"+self.windowName+str(time.time())+".bmp")
            sendToServer(str(datetime.datetime.now())[11:18]+': finish yunhun '+str(self.nowTimes)+' time')
            fan.leftclick(307, 121)
            sleep(.500)
        intX,intY = FindPic(dm,413,312,543,381,u"C:/anjianScript/通用经验/御魂确定.bmp","030303", 0.8, 0)
        if intX > 0 and intY > 0:
            fan.leftclick(intX,intY)
            sleep(.500)
        intX,intY = FindPic(dm,256,85,326,139,u"C:/anjianScript/阴阳师碎片/失败鼓.bmp","000000",0.8,0)
        if intX>0:
            global inBattle
            inBattle = False
            fan.leftclick(intX,intY)
            sleep(.500)
        return True

    def runGuiwang(self):
        while True:
            ret = self.guiwangLoop(self.dm)
            if ret == False:
                break
            sleep(2)

    def runApp(self):
        while True:
            ret = self.mainLoop(self.dm)
            if ret == False:
                break
            sleep(1)


dm1 = reg()
dm2 = reg()
moveWindowAndBind(dm1,'dahao')
moveWindowAndBind(dm2,'xiaohao')

times = 0
ishun10 = True
guiwang = False

yuhun1 = Yuhun(dm1,'dahao',times = times,ishun10 = ishun10)
yuhun2 = Yuhun(dm2,'xiaohao',times = times,ishun10 = ishun10)
t1 = threading.Thread(target = yuhun1.runApp)
t2 = threading.Thread(target = yuhun2.runApp)

if guiwang:
    dm3 = reg()
    moveWindowAndBind(dm3,'jiangshi')
    yunhun3 = Yuhun(dm3,'jiangshi',times = times,ishun10 = ishun10)
    t3 = threading.Thread(target = yunhun3.runGuiwang)
    t3.start()

t1.start()
t2.start()
while True:
    try:
        sleep(20)
    except KeyboardInterrupt:
        dm1.UnBindWindow()
        dm2.UnBindWindow()
        print 'end'
        break
