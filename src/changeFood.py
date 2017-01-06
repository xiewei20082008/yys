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
        ret = dm.FindStrFastExS(19,93,760,440,u"满",("eca614-101010|f7e447-151515|deae4a-151515"
            "|ead643-151515|f1d518-151515|e39a34-151515|ad9334-151515|f7aa4a-151515"),0.8)
        # print ret

        dm.useDict(1)
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
        sleep(1.5)
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
            sleep(1)
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
    cf.changeBattleSide()
    # cf.moveFood()
    dm.UnBindWindow()
