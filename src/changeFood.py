#coding=utf8

class ChangeFood:
    def __init__(self):
        self.startPointY = 474
        return


    def recogFull(self,dm):
        dm.useDict(0)
        ret = dm.FindStrFastExS(19,93,760,440,u"满",("eca614-101010|f7e447-151515|deae4a-151515"
            "|ead643-151515|f1d518-151515|e39a34-151515|ad9334-151515|f7aa4a-151515"),0.8)
        print ret

        dm.useDict(1)
    def findStartPoints(self,dm):
        startPoints = []
        i = 200
        while i<560:
            if dm.cmpColor(i,self.startPointY,"281408-050505",1)==0 and dm.cmpColor(i+1,self.startPointY,"281408-050505",1) !=0:
                startPoints.append(i)
            i+=1
        print startPoints    
        if len(startPoints)>=2:
            if startPoints[1] - startPoint[0]<30:
                v = [ x for index,x in enumerate(startPoints) if index % 2 ==1]
                print v
                return v
            else:
                v = [ x for index,x in enumerate(startPoints) if index % 2 ==0]
                print v
                return v
        else:
            return []

    def getLevelAverageColor(self,dm):
        levelRect = (16,13)
        def calAverage(t):
            return dm.GetAveRGB(t,self.startPointY,t+levelRect[0],self.startPointY+levelRect[1])

        startPoints = self.findStartPoints(dm)
        print startPoints
        avgColors = map(calAverage,startPoints)
        print avgColors
