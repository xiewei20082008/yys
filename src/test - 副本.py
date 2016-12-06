#coding=utf8
from time import sleep
from toolkit import *
import time
class UnionRush:
    def __init__(self,dm):
        self.dm = dm
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
            sleep(.500)
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
        return time.time()    

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
        intX,intY = FindPic(dm,298,129,733,571,u"C:/anjianScript/公会突破/attack.bmp","000000",0.8,0)
        if intX>0:
            dm.moveto(intX,intY)
            dm.leftclick()
            self.nowUnion +=1
            self.lastTime = time.time()
            sleep(.500)
        autoBattle(dm)
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
            l = int(s)
            if l<=self.acceptLevel:
                dm.moveto(i[0],i[1])
                dm.leftClick()
                sleep(.500)
                break
        dm.useDict(v)
