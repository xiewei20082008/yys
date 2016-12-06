#coding=utf8
from time import sleep
from toolkit import *
import datetime
import time
class UnionRush:
    def __init__(self,dm,windowName):
        self.dm = dm
        self.windowName = windowName
        self.levelPos = [(324,154),(324,228),(324,302),(324,376),(324,450),(527,154),(527,228),(527,303),(527,376),(527,451)]
        self.unionPos = [(266,206),(266,315),(266,425)]
        self.acceptLevel = 25
        self.nowUnion = 0
        self.lastTime = time.time()
    def rushAllUnion(self):
        dm = self.dm
        if self.nowUnion>2:
            return 0
        i = self.unionPos[self.nowUnion]
        ret = dm.getcolor(i[0],i[1])
        if ret == "685a4f":
            dm.moveto(i[0],i[1])
            dm.leftClick()
            sleep(1.500)
            self.recogLevel()
            sleep(1)
            return 1
        else:
            self.nowUnion +=1
            return 1
    def runUp(self):
        while True:
            if time.time() - self.lastTime >90:
                print 'union timeout'
                break
            ret = self.main()
            if ret == 0:
                break
            sleep(1)
        return True

    def main(self):
        dm = self.dm
        intX,intY = FindPic(dm,758,259,783,315,u"C:/anjianScript/公会突破/公会tab.bmp","000000",0.8,0)
        if intX>0:
            dm.moveto(intX,intY)
            dm.leftClick()
            sleep(.500)
        intX,intY = FindPic(dm,759,259,780,316,u"C:/anjianScript/公会突破/公会tabLight.bmp","000000",0.8,0)
        if intX>0:
            ret = self.rushAllUnion()
            return ret

        autoBattle(dm,shenLe=True)
        return 1
    def testRecog(self):
        dm = self.dm
        v = dm.getNowDict()
        dm.useDict(2)
        for i in self.levelPos:
            s = dm.Ocr(i[0],i[1],i[0]+14,i[1]+11,"b@2b2118-606060",0.8)
            print s
        dm.useDict(v)

    def recogLevel(self):
        dm = self.dm
        # dm.Capture(0,0,500,400,"c:/screen.bmp")
        v = dm.getNowDict()
        dm.useDict(2)
        for i in self.levelPos:
            s = dm.Ocr(i[0],i[1],i[0]+14,i[1]+11,"b@2b2118-606060",0.8)
            l = 100
            if s.isdigit():
                l = int(s)
            if l<=self.acceptLevel:
                dm.moveto(i[0],i[1])
                dm.leftClick()
                sleep(.500)#到点攻击的地方
                dm.moveR(130,80)
                dm.leftclick()
                sleep(.500)
                sendToServer(str(datetime.datetime.now())[11:18]+"|"+str(self.windowName)+"|Attack Union "+str(self.nowUnion) )
                self.lastTime = time.time()
                sleep(.500)
                break
        self.nowUnion +=1
        self.lastTime = time.time()
        dm.useDict(v)
