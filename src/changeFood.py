#coding=utf8
from toolkit import *
from time import sleep

class ChangeFood:
    def __init__(self):
        self.startPointY = 474
        self.battleOffset = (274-249,519-474)
        self.battleSize = (63,63)
        return


    def recogFull(self,dm):
        dm.useDict(0)
        ret = dm.FindStrFastExS(19,93,760,440,u"满",("eca614-101010|f7e447-151515|deae4a-151515"
            "|ead643-151515|f1d518-151515|e39a34-151515|ad9334-151515|f7aa4a-151515"),0.8)
        print ret

        dm.useDict(1)
    def findStartPoints(self,dm):
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
                print v
                return v
            else:
                v = [ x for index,x in enumerate(startPoints) if index % 2 ==0]
                print v
                return v
        else:
            return []
    def moveFood(self,dm):
        start = (296,525)
        end = (131,247)
        dm.moveto(start[0],start[1])
        dm.leftdown()
        dragMoveTo(dm,start,(start[0],end[1]))
        dragMoveTo(dm,(start[0],end[1]),end)
        dm.leftup()
        sleep(1)
    def changeOneSide(self,dm,num,aimPos):
        for i in range(num):
            endPos = aimPos[i]
            startPos = getMoveablePos()
            dm.moveto(startPos[0],startPos[1])
            dm.leftdown()
            dragMoveTo(dm,start,(startPos[0],endPos[1]))
            dragMoveTo(dm,(startPos[0],endPos[1]),endPos)
            dm.leftup()
            sleep(1)


    def getLevelAverageColor(self,dm):
        levelRect = (15,13)
        def calAverage(t):
            return dm.GetAveRGB(t,self.startPointY,t+levelRect[0],self.startPointY+levelRect[1])
        def isMoveable(t):
            ret = dm.GetAveRGB(t,self.startPointY,t+levelRect[0],self.startPointY+levelRect[1])
            print ret
            if int(ret[4:],16) > 0x30:
                print 'no full'
            else:
                print 'full'
                return False

            x = t+self.battleOffset[0]
            y = self.startPointY+self.battleOffset[1]
            intX,intY = FindPic(dm,x,y,x+self.battleSize[0],y+self.battleSize[1],
                u"C:/anjianScript/通用经验/战.bmp|C:/anjianScript/通用经验/观.bmp","404040",0.7,0)
            if intX >0:
                print 'find zhan'
                return False
            else:
                print 'no find zhan'
                return True

        startPoints = self.findStartPoints(dm)
        print startPoints
        moveableFoods = map(isMoveable,startPoints)
        # if int(avgColors[4:],16)>0x30:
        #     print 'no full'
        # else:
        #     print 'full'

        print moveableFoods
if __name__ == "__main__":
    dm = reg()
    moveWindowAndBind(dm,'dahao')
    cf = ChangeFood()
    cf.
    dm.UnBindWindow()
