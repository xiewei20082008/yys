#coding=utf8
import threading
from toolkit import *
from time import sleep

class Manager():
    def __init__(self):
        self.dm_manager = reg()
        self.dm_dahao = reg()
        self.dm_xiaohao= reg()
        self.hwnd = 0
    def bindWindow(self):
        dm = self.dm_manager
        hwnd = dm.FindWindow("",u"天天模拟器管理")
        self.hwnd = hwnd
        print hwnd
        ret = dm.BindWindow(hwnd, "normal", "normal", "normal", 0)
        if ret!=1:
            print 'bind error'
            print dm.getlasterror()
            return
    def restart1(self,x,y):
        self.showAhead()
        dm = self.dm_manager
        dm.setPath(u"c:/anjianScript/通用经验")
        for i in range(0,10):
            print 'here'
            # intX,intY = FindPic(dm,x,y,x+90,y+50,u"启动.bmp|启动1.bmp","050505",0.8,0)
            intX,intY = FindPic(dm,x,y,x+90,y+50,u"启动.bmp","050505",0.8,0)
            if intX>0:
                print 'find qidong'
                dm.moveto(intX,intY)
                dm.leftclick()
                sleep(.500)
                dm.moveto(0,0)
                sleep(1.500)
                break
            intX,intY = FindPic(dm,x,y,x+90,y+50,u"关闭.bmp","050505",0.8,0)
            if intX>0:
                dm.moveto(intX,intY)
                dm.leftclick()
                sleep(.500)
                dm.moveto(0,0)
                sleep(7.0)

                continue
            sleep(2.0)
    # def restartXiaohao(self):
    #     self.restart(329,88)
    def restart(self,windowName):
        if windowName == "dahao":
            self.restart1(329,186)
        elif windowName == "xiaohao":
            self.restart1(329,88)
    # def restartJiangshi(self):
    #     self.restart(329,136)
    def showAhead(self):
        ret = self.dm_manager.SetWindowState(self.hwnd,7)
        ret = self.dm_manager.SetWindowState(self.hwnd,1)
        sleep(2.0)
    def tryBind(self,windowName):
        dm = 0
        if windowName== "dahao":
            dm = self.dm_dahao
        elif windowName== "xiaohao":
            dm = self.dm_xiaohao
        for i in range(0,10):
            hwnd = dm.FindWindow("",windowName)
            if hwnd>0:
                hwndGame = dm.EnumWindow(hwnd,"kaopu","",1+16)
                print hwndGame
                if hwndGame.isdigit()  and hwndGame>0:
                    ret = dm.BindWindow(hwndGame, "dx2", "windows", "normal", 0)
                    if ret ==1:
                        print 'bind OK'
                        setDict(dm)
                        return True
            sleep(3)
        else:
            return False
    # dm.MoveWindow(hwnd, -2 , -38)
    # ret = dm.MoveWindow(hwnd, -2 , -38)
    def test(self,windowName):
        dm = 0
        if windowName== "dahao":
            dm = self.dm_dahao
        elif windowName== "xiaohao":
            dm = self.dm_xiaohao
        dm.setPath(u"c:/anjianScript/通用经验")
        print 'start find'
        chapter =5
        dm_ret = dm.Capture(0,0,800,600,"d:/screen.bmp")
        print dm_ret
        intX,intY = FindPic(dm,537,53,635,157,u"阴阳师图标.bmp","202020",0.8,0)
        print intX,intY
        print 'find end'
        # if intX>0:
            # print 'found'
            # dm.moveto(intX,intY)
            # dm.leftClick()
            # sleep(.500)

    def tryInit(self,windowName,chapter):
        dm = 0
        if windowName== "dahao":
            dm = self.dm_dahao
        elif windowName== "xiaohao":
            dm = self.dm_xiaohao
        dm.setPath(u"c:/anjianScript/通用经验")
        for i in range(0,15):


            intX,intY = FindPic(dm,673,69,799,404,u"第"+str(chapter)+u"章.bmp","606060",0.7,0)
            if intX>0:
                print 'find'
                dm.moveto(intX,intY)
                dm.leftClick()
                sleep(.500)
                return True

            else:
                dm.moveto(728,235)
                sleep(.500)
                dm.wheelup()
                sleep(.500)

            intX,intY = FindPic(dm,534, 366,653, 441,u"C:/anjianScript/通用经验/探索页.bmp","000000",0.7,0)
            if intX > 0:
                dm.moveto(659,163)
                dm.leftClick()
                sleep(.500)
                return True

            sleep(2.5)
        else:
            return False

    def tryEnterGame(self,windowName):
        dm = 0
        if windowName== "dahao":
            dm = self.dm_dahao
        elif windowName== "xiaohao":
            dm = self.dm_xiaohao
        dm.setPath(u"c:/anjianScript/通用经验")
        print 'in enter game'
        for i in range(0,40):
            intX,intY = FindPic(dm,537,53,635,157,u"阴阳师图标.bmp","202020",0.8,0)
            if intX>0:
                print 'find icon'
                dm.moveto(intX,intY)
                dm.leftclick()
                sleep(.500)


            intX,intY = FindPic(dm,700,0,750,50,u"邮件.bmp","000000",0.8,0)
            if intX>0:
                sleep(5.0)
                dm.moveto(431,103)
                dm.leftClick()
                sleep(7.0)
                print 'enter game ok'
                return True

            if dm.cmpColor(730,20,"d6c7a5-0a0a0a",1) !=0:
                print 'click once'
                dm.moveto(397,441)
                dm.leftclick()
                sleep(.500)

            sleep(1.5)
        else:
            return False



    def close(self):
        self.dm_manager.unbindwindow()
        self.dm_dahao.unbindwindow()
        self.dm_xiaohao.unbindwindow()
        print 'end'

class Script:
    def __init__(self):
        self.threadEntity = 0
        self.dm = 0
        self.lastActiveTime = 0
        self.mutex = threading.Lock()

class Deamon:
    def __init__(self):
        self.m = Manager()
        self.m.bindWindow()
    def startWindow(self,windowName,chapter):
        self.m.restart(windowName)
        ret = self.m.tryBind(windowName)
        ret = self.m.tryEnterGame(windowName)
        ret = self.m.tryInit(windowName,chapter)
    def close(self):
        self.m.close()
