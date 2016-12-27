#coding=utf8
import threading
import ExpElf
import time
from toolkit import *
from time import sleep
import Client
from pymouse import PyMouse

class Manager():
    def __init__(self):
        self.dm_manager = reg()
        self.dm_dahao = reg()
        self.dm_xiaohao= reg()

        self.dm_manager.SetShowErrorMsg(0)
        self.dm_dahao.SetShowErrorMsg(0)
        self.dm_xiaohao.SetShowErrorMsg(0)
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
                sleep(1.000)
                mouse = PyMouse()
                mouse.move(1,1)
                sleep(1.500)
                break
            intX,intY = FindPic(dm,x,y,x+90,y+50,u"关闭.bmp","050505",0.8,0)
            if intX>0:
                dm.moveto(intX,intY)
                dm.leftclick()
                sleep(.500)
                dm.moveto(0,0)
                sleep(4.0)

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
        for i in range(0,20):
            hwnd = dm.FindWindow("",windowName)
            if hwnd>0:
                hwndGame = dm.EnumWindow(hwnd,"kaopu","",1+16)
                print hwndGame
                if hwndGame.isdigit()  and hwndGame>0:
                    dm.ForceUnBindWindow(hwndGame)
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


            intX,intY = FindPic(dm,673,69,799,404,u"第"+str(chapter)+u"章.bmp","202020",0.8,0)
            if intX>0:
                print 'find'
                dm.moveto(intX,intY)
                dm.leftClick()
                sleep(2.500)

            else:
                dm.moveto(728,150)
                sleep(.500)

                dm.leftdown()
                sleep(1.000)
                for i in range(0,3):
                    dm.mover( 0, 30)
                    sleep(.200)

                sleep(1.000)
                dm.leftup()
                sleep(.300)
                dm.leftup()
                sleep(1.500)


            sleep(1.0)

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
                sleep(7.0)
                dm.moveto(428,264)
                dm.leftclick()
                sleep(.500)

            intX,intY = FindPic(dm,444,318,509,361,u"更新确定.bmp","050505",0.8,0)
            if intX>0:
                print 'update'
                dm.moveto(intX,intY)
                dm.leftclick()
                sleep(.500)

            intX,intY = FindPic(dm,646,170,688,209,u"更新叉.bmp","050505",0.8,0)
            if intX>0:
                print 'cross'
                dm.moveto(intX,intY)
                dm.leftclick()
                sleep(.500)

            intX,intY = FindPic(dm,700,0,750,50,u"邮件.bmp","000000",0.8,0)
            if intX>0:
                sleep(5.0)
                dm.moveto(336,154)
                dm.leftClick()
                sleep(7.0)
                print 'enter game ok'
                return True

            intX,intY = FindPic(dm,120,210,168,266,u"服务器选择.bmp","030303",0.8,0)
            if intX>0:
                print 'chosse server start'
                sleep(2.0)
                dm.moveto(347,273)
                dm.leftClick()
                sleep(5.0)
                dm.moveto(195,458)
                dm.leftClick()
                sleep(1.5)
                dm.moveto(201,412)
                dm.leftClick()
                sleep(1.500)
                dm.moveto(400,442)
                #点击开始游戏
                dm.leftClick()
                sleep(7.000)
                dm.moveto(400,442)
                dm.leftclick()
                sleep(.500)
                print 'choose server ok'

            # if dm.cmpColor(730,20,"d6c7a5-0a0a0a",1) !=0:
            #     print 'click once'
            #     dm.moveto(601,202)
            #     dm.leftclick()
            #     sleep(2.500)

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
        self.lastAliveTime = 0
        self.mutex = threading.Lock()
        self.elf = None

class Deamon:
    def __init__(self):
        self.m = Manager()
        self.m.bindWindow()
        self.xiaohaoScript = Script()
        self.dahaoScript = Script()
    def startWindow(self,windowName,chapter):
        sendToServer(windowName+' try to enter game')
        self.m.restart(windowName)
        ret = self.m.tryBind(windowName)
        if not ret:
            return ret
        ret = self.m.tryEnterGame(windowName)
        if not ret:
            return ret
        ret = self.m.tryInit(windowName,chapter)
        if not ret:
            return ret
        sendToServer(windowName+' enter game successfully')
        return True
    def close(self):
        self.m.close()
    def runUp(self):

        def resetScript(script):
            if script.elf is not None:
                script.elf.gameOver = True
            script.mutex.acquire()
            script.lastAliveTime = 0
            script.mutex.release()
            script.elf = None
            return
        def openWindowAndRun(windowName,script,dm):
            def isScriptNeedRestart():
                if script.elf is not None and script.elf.gameOver is True:
                    resetScript(script)
                    sendToServer(windowName+': restart for gameOver')
                    return True
                elif script.lastAliveTime ==0:
                    sendToServer(windowName+': restart for lastAliveTime is zero')
                    return True
                elif time.time() - script.lastAliveTime > 15*60:
                    sendToServer(windowName+': restart for script timeout')
                    dm.Capture(0,0,800,600,'f:/timeoutPic/'+str(time.time())+'.bmp')
                    resetScript(script)
                    return True
                else:
                    return False


            commandFile = open('c:/anjianScript/'+windowName+'.txt','r')
            command = commandFile.readline()
            commandFile.close()
            state,chapter,aimEnergy,isRush = command.split(' ')
            print state,chapter,aimEnergy,isRush
            if state == "0":
                if script.lastAliveTime is not 0 and script.elf is not None:
                    script.elf.gameOver = True
                    script.mutex.acquire()
                    script.lastAliveTime = 0
                    script.mutex.release()
                    sendToServer(windowName+" has stopped.(full)")
                return True
            elif state=="1":
                if isScriptNeedRestart():
                    # 运行到初始状态
                    ret = self.startWindow(windowName,int(chapter))
                    if ret:
                        print u'窗口启动成功'
                        script.mutex.acquire()
                        script.lastAliveTime = time.time()
                        script.mutex.release()
                    else:
                        print u'窗口启动失败'
                        return False
                    elf = 0
                    script.dm = dm
                    evalString = 'ExpElf.ExpElf(self.m.dm_'+windowName+',"'+windowName+'",'+chapter+','+aimEnergy+',isRush = '+isRush+',script=script)'
                    print evalString
                    elf = eval(evalString)
                    script.elf = elf
                    t1 = threading.Thread(target = elf.runUp)
                    script.threadEntity = t1
                    t1.start()
                    return True
                else:
                    # f = open('d:/lastAliveTimegap.txt','a')
                    # print >>f, time.time() - script.lastAliveTime
                    # f.close()
                    return True


        client = Client.Client()
        thread_client = threading.Thread(target = client.sendHeartbeat)
        thread_client.start()
        while True:
            ret = openWindowAndRun("xiaohao",self.xiaohaoScript,self.m.dm_xiaohao)
            if not ret:
                continue
            ret = openWindowAndRun("dahao",self.dahaoScript,self.m.dm_dahao)
            if not ret:
                continue
            sleep(10.0)

d = Deamon()
d.runUp()
