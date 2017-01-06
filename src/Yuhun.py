#coding=utf8
from toolkit import *
from time import sleep
import datetime
import time
import threading
class Yuhun:
    def __init__(self,dm,windowName,times = 0):
        self.dm = dm
        self.windowName = windowName
        self.times = times
        self.add = 1
        self.nowTimes = 0
        self.fan = Fan(dm,windowName)

    def mainLoop(self,dm,fan = None):
        if not fan:
            fan = self.fan
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
            fan.leftclick(724,500)
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
            dm.Capture(0,0,800,600,"c:/bonus/"+self.windowName+str(time.time())+".bmp")
            sendToServer(str(datetime.datetime.now())+': finish yunhun '+str(self.nowTimes)+' time')
            fan.leftclick(307, 121)
            sleep(.500)
        intX,intY = FindPic(dm,413,312,543,381,u"C:/anjianScript/通用经验/御魂确定.bmp","030303", 0.8, 0)
        if intX > 0 and intY > 0:
            fan.leftclick(intX,intY)
            sleep(.500)
        return True

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

yuhun1 = Yuhun(dm1,'dahao')
yuhun2 = Yuhun(dm2,'xiaohao')
t1 = threading.Thread(target = yuhun1.runApp)
t2 = threading.Thread(target = yuhun2.runApp)

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