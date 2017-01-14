#coding=utf8
from toolkit import *
class AutoHun10:
    def __init__(self,dm,windowName):
        self.dm = dm
        self.windowName = windowName
        self.fan = Fan(dm,windowName)
        self.shifaguiTry = 0
        self.failNum = 0
    def mainLoop(self):
        fan = self.fan
        dm = self.dm

        intX,intY = FindPic(dm,18,501,36,523,u"C:/anjianScript/通用经验/战斗指南针.bmp","000000",0.8,0)
        if intX>0:
            fan.leftclick(intX,intY)
            sleep(1)

        intX,intY = FindPic(dm,659,534,718,598,u"C:/anjianScript/通用经验/兔子跳.bmp|C:/anjianScript/通用经验/兔子跳1.bmp","030303",1,0)
        if intX > 0 and intY > 0:
            fan.leftclick(685,569)
            sleep(.230)
            fan.leftclick(718,424)
            sleep(.150)
            self.shifaguiTry = 0
            return 1
        intX,intY = FindPic(dm,612,555,626,569,u"C:/anjianScript/通用经验/源的回合.bmp","030303",1,0)
        if intX > 0 and intY > 0:

            intX,intY = FindPic(dm,538,104,669,235,u"C:/anjianScript/通用经验/萤草球.bmp","101010",0.9,0)
            if intX > 0 and intY > 0:
                fan.leftclick(685,567)
                sleep(.150)
                fan.leftclick(605,161)
                sleep(.150)

            else:
                fan.leftclick(35,564)
                sleep(.250)
                fan.leftclick(35,564)
                sleep(.500)
            return 1
        intX,intY = FindPic(dm,719,529,798,604,u"C:/anjianScript/通用经验/打火机回合.bmp|C:/anjianScript/通用经验/打火机回合1.bmp","030303",1,0)
        if intX > 0 and intY > 0:
            fan.leftclick(749,554)
            sleep(.150)
            fan.leftclick(718,424)
            sleep(.150)
            return 1
        intX,intY = FindPic(dm,720,534,795,596,u"C:/anjianScript/通用经验/食发鬼回合.bmp|C:/anjianScript/通用经验/食发鬼回合1.bmp","030303",1,0)
        if intX > 0 and intY > 0:
            clickPos = {0:(389,148),1:(174,164),2:(591,167)}
            fan.leftclick(749,552)
            sleep(.050)
            fan.leftclick(clickPos[self.shifaguiTry][0],clickPos[self.shifaguiTry][1])
            self.shifaguiTry = (self.shifaguiTry+1)%3
            sleep(.600)
            return 1
        intX,intY = FindPic(dm,720,534,795,596,u"C:/anjianScript/通用经验/食发鬼断火.bmp","030303",1,0)
        if intX > 0 and intY > 0:
            fan.leftclick(35,564)
            sleep(.250)
            fan.leftclick(35,564)
            sleep(.500)
            return 1
        intX,intY = FindPic(dm,677,554,698,575,u"C:/anjianScript/通用经验/兔子断火.bmp","030303",1,0)
        if intX > 0 and intY > 0:
            fan.leftclick(35,564)
            sleep(.250)
            fan.leftclick(35,564)
            sleep(.500)
            return 1

        intX,intY = FindPic(dm,13,549,60,584,u"C:/anjianScript/通用经验/自动.bmp","000000",0.8,0)
        if intX>0:
            fan.leftclick(intX,intY)
            sleep(1)


        intX,intY = FindPic(dm,227,46,385,190,u"C:/anjianScript/阴阳师碎片/胜利鼓.bmp","000000", 0.9, 0)
        if intX > 0 and intY > 0:
            return 0

        intX,intY = FindPic(dm,256,85,326,139,u"C:/anjianScript/阴阳师碎片/失败鼓.bmp","000000",0.8,0)
        if intX>0:
            fan.leftclick(intX,intY)
            self.failNum+=1
            if self.failNum==4:
                sleep(60000)
            sleep(.500)
            return 0
        return 1


if __name__ == '__main__':
    dm = reg()
    moveWindowAndBind(dm,'dahao')
    ah = AutoHun10(dm,'dahao')
    # moveWindowAndBind(dm,'xiaohao')
    # ah = AutoHun10(dm,'xiaohao')
    while True:
        ret = ah.mainLoop()
        sleep(.200)
        a = dm.getkeystate(83)
        if a==1:
            print 's down'
            break
    dm.UnBindWindow()
