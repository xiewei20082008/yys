#coding=utf8
from toolkit import *
from time import sleep
class YaoQiFengYin:
    def __init__(self):
        self.dm = reg()
        ret = self.dm.BindWindow(605170, "normal", "normal", "normal", 0)
    def find(self):
        dm = self.dm
        while True:
            a = dm.getkeystate(83)
            if a==1:
                print 's down'
                break
            intX,intY = FindPic(dm,221,145,408,391,u"c:/anjianScript/通用经验/椒图.bmp","101010",0.9,0)
            if intX>0:
                dm.moveto(660,intY+20)
                dm.leftclick()
                sleep(.500)
        dm.UnBindWindow()

fy = YaoQiFengYin()
fy.find()
