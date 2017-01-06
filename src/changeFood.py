#coding=utf8
from toolkit import *
from time import sleep

class ChangeFood:
    def __init__(self,dm,windowName):
        self.startPointY = 474
        self.battleOffset = (274-249,519-474)
        self.dm = dm
        self.battleSize = (63,63)
        self.fan = Fan(dm,windowName)
        return


    def recogFull(self):
        dm = self.dm
        dm.useDict(0)
        dm.SetExactOcr(1)

        ret = FindMultiPic(dm,62,129,674,402,(u"C:/anjianScript/通用经验/满.bmp|"
            u"C:/anjianScript/通用经验/满1.bmp"),"080808",1,0)
        # ret = dm.FindStrExS(19,93,760,440,u"满",("f4c31b-303030|e3a943-303030|997a29-202020"),0.5)
        # print ret
        print ret


        dm.useDict(1)
        dm.SetExactOcr(0)
        return ret
    def startChange(self):
        dm = self.dm
        fan = self.fan
        _method_change = None
        sleep(5)
        while True:
            intX,intY = FindPic(dm,13,490,38,522,u"C:/anjianScript/通用经验/战斗灯笼.bmp","030303",0.9,0)
            if intX >0:
                print 'find denlonog'
                ret = self.recogFull()
                if not ret:
                    fan.leftclick(726,505) # 准备
                    sleep(1)
                    break
                elif any (i[0]<195 for i in ret ):
                    print 'change watch'
                    fan.leftclick(152,268)
                    sleep(.500)
                    _method_change = self.changeWatchSide
                    sleep(3.0)
                else:
                    print 'change battle'
                    fan.leftclick(440,401)
                    sleep(.500)
                    _method_change = self.changeBattleSide
                    sleep(3.0)

            intX,intY = FindPic(dm,23,474,59,514,u"C:/anjianScript/通用经验/换狗粮N.bmp","030303",0.9,0)
            if intX>0:
                print 'n correct start change one side'
                if _method_change:
                    _method_change()
                else:
                    sendToServer('change one side but func is None!!')
                    return False
                sleep(1.0)
                fan.leftclick(24,27)
                sleep(3.000)
            intX,intY = FindPic(dm,16,474,65,514,(u"C:/anjianScript/通用经验/换狗粮R.bmp|"
                u"C:/anjianScript/通用经验/换狗狼全部.bmp"),"030303",0.9,0)
            if intX>0:
                fan.leftclick(41,491)
                sleep(1)
                fan.leftclick(40,354)
                sleep(2)



            sleep(1)
        print 'change end'
        return True

    def findStartPoints1(self):
        dm = self.dm
        count = 0
        x = None
        lastColor = None
        startPoints = []
        for i in range(230,600):
            ret = dm.getcolor(i,self.startPointY)
            if lastColor == None:
                lastColor = ret
                x = i
                count = 0
            elif isColorSimiliar(ret,lastColor,8):
                count+=1
            else:
                if count>35:
                    count = 0
                    startPoints.append(i-70)
                lastColor = ret
                x = i
        return startPoints





    def findStartPoints(self):
        dm = self.dm
        startPoints = []
        i = 183
        while i<560:
            if dm.cmpColor(i,self.startPointY,"281408-050505",1)==0 and dm.cmpColor(i+1,self.startPointY,"281408-050505",1) !=0:
                startPoints.append(i)
            i+=1
        print startPoints
        if len(startPoints)>=2:
            if startPoints[1] - startPoints[0]<30:
                v = [ x for index,x in enumerate(startPoints) if index % 2 ==1]
                # print v
                return v
            else:
                v = [ x for index,x in enumerate(startPoints) if index % 2 ==0]
                # print v
                return v
        else:
            return []
    def moveFood(self,start,end):
        dm = self.dm
        fan = self.fan
        # dm.moveto(start[0],start[1])
        fan.leftdown(start[0],start[1])
        sleep(.500)
        # fan.leftdownmove(start[0],end[1])
        # fan.leftdownmove(end[0],end[1])
        # sleep(1.500)
        dragMoveTo(fan,start,(start[0],end[1]))
        dragMoveTo(fan,(start[0],end[1]),end)
        sleep(.300)
        fan.leftup(start[0],end[1])
        # dm.leftup()
        sleep(1)
    def changeOneSide(self,num,aimPos):
        dm = self.dm
        nowNum = 0
        while nowNum<num:
            moveablePos = self.getMoveablePos()
            for i in moveablePos:
                self.moveFood((i+30,self.startPointY+50),aimPos[nowNum])
                nowNum+=1
                if nowNum==num:
                    break
            self.changePage()
    def changePage(self):
        print 'changePagestart'
        dm = self.dm
        fan = self.fan
        start = (575,536)
        end = (300,536)
        dm.moveto(start[0],start[1])
        fan.leftdown(start[0],start[1])
        # dm.leftdown()
        sleep(.500)
        dragMoveTo(fan,start,end)
        fan.leftup(end[0],end[1])
        # dm.leftup()
        sleep(1)
        print 'changePageend'

    def changeBattleSide(self):
        aimPos = ((130,277),(410,265),(685,254))
        self.changeOneSide(3,aimPos)
    def changeWatchSide(self):
        aimPos = ((197,248),(535,214))
        self.changeOneSide(2,aimPos)


        # for i in range(num):
        #     endPos = aimPos[i]
        #     startPos = getMoveablePos()
        #     dm.moveto(startPos[0],startPos[1])
        #     dm.leftdown()
        #     dragMoveTo(dm,start,(startPos[0],endPos[1]))
        #     dragMoveTo(dm,(startPos[0],endPos[1]),endPos)
        #     dm.leftup()
        #     sleep(1)


    def getMoveablePos(self):
        dm = self.dm
        levelRect = (15,13)
        def calAverage(t):
            return dm.GetAveRGB(t,self.startPointY,t+levelRect[0],self.startPointY+levelRect[1])
        def isMoveable(t):
            ret = dm.GetAveRGB(t,self.startPointY,t+levelRect[0],self.startPointY+levelRect[1])
            # print ret
            if int(ret[4:],16) > 0x30:
                pass
                # print 'no full'
            else:
                # print 'full'
                return False

            x = t+self.battleOffset[0]
            y = self.startPointY+self.battleOffset[1]
            intX,intY = FindPic(dm,x,y,x+self.battleSize[0],y+self.battleSize[1],
                u"C:/anjianScript/通用经验/战.bmp|C:/anjianScript/通用经验/观.bmp","0a0a0a",1,0)
            if intX >0:
                # print 'find zhan'
                return False
            else:
                # print 'no find zhan'
                return True

        startPoints = self.findStartPoints1()
        print startPoints
        moveableFoods = map(isMoveable,startPoints)
        # if int(avgColors[4:],16)>0x30:
        #     print 'no full'
        # else:
        #     print 'full'

        print 'moveablefood'
        print moveableFoods
        moveablePos = []
        for index,value in enumerate(moveableFoods):
            if value:
                moveablePos.append(startPoints[index])
        print moveablePos
        return moveablePos
if __name__ == "__main__":
    dm = reg()
    moveWindowAndBind(dm,'dahao')
    cf = ChangeFood(dm,'dahao')
    # ret = cf.findStartPoints()
    # print ret
    # print 'next'
    # ret = cf.findStartPoints1()
    # print ret
    # cf.getMoveablePos()
    # start = (297,529)
    # end = (197,300)
    # cf.moveFood(start,end)
    ret = cf.startChange()
    print ret
    # cf.changeWatchSide()
    # cf.moveFood()
    dm.UnBindWindow()
