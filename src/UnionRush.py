#coding=utf8
from time import sleep
from toolkit import *
import datetime
import time
class UnionRush:
    def __init__(self,dm,windowName):
        self.dm = dm
        self.windowName = windowName
        self.levelPos = [(324,154),(324,228),(324,302),(324,376),(527,154),(527,228),(527,303),(527,376)]
        # self.levelPos = [(324,154),(324,228),(324,302),(324,376),(324,450),(527,154),(527,228),(527,303),(527,376),(527,451)]
        self.unionPos = [(266,206),(266,315),(266,425)]
        self.acceptLevel = 25
        self.nowUnion = 0
        self.lastTime = time.time()
    def exitRush(self):
        dm = self.dm
        for i in range (0,30):
            intX,intY = FindPic(dm,223,525,320,601,u"C:/anjianScript/通用经验/起始页.bmp|C:/anjianScript/通用经验/起始页1.bmp","000000",0.9,0)
            if intX > 0 and intY > 0:
                return True
            intX,intY = FindPic(dm,300,50,460,150,u"C:/anjianScript/通用经验/顶部结界突破.bmp|C:/anjianScript/通用经验/顶部结界突破1.bmp","050505",0.8,0)
            if intX > 0 and intY > 0:
                dm.moveto(63,566)
                dm.leftClick()
                sleep(1.0)
                continue
            sleep(.500)
        else:
            return False
    def rushAllUnion(self):
        dm = self.dm
        if self.nowUnion>2:
            ret = self.exitRush()
            return ret
        i = self.unionPos[self.nowUnion]
        ret = dm.getcolor(i[0],i[1])
        if ret == "685a4f":
            dm.moveto(i[0],i[1])
            dm.leftClick()
            sleep(2.500)
            self.recogLevel()
            sleep(1)
            return False
        else:
            self.nowUnion +=1
            return False
    def runUp(self):
        while True:
            if time.time() - self.lastTime >90:
                ret = self.exitRush()
                if ret:
                    return True
            ret = self.main()
            if ret :
                return True
            sleep(1)
        return True
    def findFirstY(self):
        dm = self.dm
        x = 503
        y = 135
        # 找到第一个白点区域
        while y<300:
            ret = dm.GetColor(x,y)
            try:
                if int(ret[4:],16)>=0xa0:
                    break
            except:
                return 0
            y+=1
        else:
            return 0
        while y<300:
            ret = dm.GetColor(x,y)
            try:
                if int(ret[4:],16)<0xa0:
                    break
            except:
                return 0
            y+=1
        else:
            return 0
        print 'result is ' + str(y)
        return y
    def main(self):
        dm = self.dm
        intX,intY = FindPic(dm,758,259,783,315,u"C:/anjianScript/公会突破/公会tab.bmp","000000",0.8,0)
        if intX>0:
            dm.moveto(intX,intY)
            dm.leftClick()
            sleep(.500)
        intX,intY = FindPic(dm,759,259,780,316,u"C:/anjianScript/公会突破/公会tabLight.bmp","000000",0.8,0)
        if intX>0:
            sleep(1.0)
            ret = self.rushAllUnion()
            return ret

        autoBattle(dm,shenLe=True)
        return False
    def testRecog(self):
        dm = self.dm
        v = dm.getNowDict()
        dm.useDict(2)
        # s = dm.OcrExOne(324,124,324+14,480,"b@2b2118-606060",0.8)
        s = dm.OcrExOne(527,124,527+14,480,"b@2b2118-606060",0.8)
        print s
        dm.useDict(v)

    def recogLevel(self):
        dm = self.dm
        # dm.Capture(0,0,500,400,"c:/screen.bmp")
        v = dm.getNowDict()
        dm.useDict(2)
        for i in range(0,5):
            y = self.findFirstY()
            if y == 0:
                break
            diff_y = y - 138
            for i in self.levelPos:
                shift_y = diff_y+i[1]
                s = dm.Ocr(i[0],shift_y,i[0]+14,shift_y+11,"b@2b2118-606060",0.8)
                l = 100
                if s.isdigit():
                    l = int(s)
                if l<=self.acceptLevel:
                    dm.moveto(i[0],shift_y)
                    dm.leftClick()
                    sleep(1.5)#到点攻击的地方
                    #here just log test
                    f = open('d:/color.txt','a+')
                    ret = dm.getcolor(i[0]+106,shift_y+82)
                    print >>f,ret
                    if dm.cmpColor(i[0]+106,shift_y+82,"f7b25a",0.8) !=0:
                        break
                    #
                    dm.moveto(i[0]+106,shift_y+82)
                    dm.leftclick()
                    sleep(.500)
                    sendToServer(str(datetime.datetime.now())[11:18]+"|"+str(self.windowName)+"|Attack Union "+str(self.nowUnion) )
                    self.lastTime = time.time()
                    sleep(.500)
                    break
            else:
                if dm.CmpColor(646,450,"67615a",0.9) ==0:
                    break
                dm.moveto(450,300)
                sleep(.300)
                dm.wheeldown()
                sleep(3.0)
                continue
            break
        self.nowUnion +=1
        self.lastTime = time.time()
        dm.useDict(v)

if __name__ == "__main__":
    dm = reg()
    try:
        moveWindowAndBind(dm,"dahao")
        ur = UnionRush(dm,"dahao")
        ur.findFirstY()
        # ur.testRecog()
    except:
        dm.unbindwindow()
