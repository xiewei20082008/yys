#coding=utf8
import win32com.client
from time import sleep
import os
import datetime
import pythoncom
import Client
import threading
from ctypes import *
import win32con
import win32api
import pywintypes


dm_send = None

client = Client.Client()
t_client = threading.Thread(target = client.send)
t_client.start()

class Fan:
    def __init__(self,dm,windowName):
        self.hwnd = dm.GetBindWindow()
        self.pyhwnd = pywintypes.HANDLE(int(self.hwnd))
    def leftclick(self,x,y):
        lParam = y <<16 | x
        win32api.SendMessage(self.pyhwnd, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON, lParam);
        sleep(.050)
        win32api.SendMessage(self.pyhwnd,win32con.WM_LBUTTONUP, 0,lParam);
    def leftdownmove(self,x,y):
        lParam = y <<16 | x
        win32api.SendMessage(self.pyhwnd, win32con.WM_MOUSEMOVE,win32con.MK_LBUTTON, lParam);
        sleep(.050)
    def leftdown(self,x,y)    :
        lParam = y <<16 | x
        win32api.SendMessage(self.pyhwnd, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON, lParam);
        sleep(.050)
    def leftup(self,x,y)    :
        lParam = y <<16 | x
        win32api.SendMessage(self.pyhwnd,win32con.WM_LBUTTONUP, 0,lParam);
        sleep(.050)
    def showHwnd(self):
        print self.hwnd

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
def isColorSimiliar(col1,col2,sim):
    def rgbSim(a,b,sim):
        return abs(a-b)<=sim
    c1_1 = int(col1[0:2],16)
    c1_2 = int(col1[2:4],16)
    c1_3 = int(col1[4:6],16)
    c2_1 = int(col2[0:2],16)
    c2_2 = int(col2[2:4],16)
    c2_3 = int(col2[4:6],16)

    if rgbSim(c1_1,c2_1,sim) and rgbSim(c1_2,c2_2,sim) and rgbSim(c1_3,c2_3,sim):
        return True
    else:
        return False
def dragMoveTo(fan,start,end):
    # sleep(.500)
    times = 10.0
    diff_x = (end[0]-start[0])/times
    diff_y = (end[1]-start[1])/times
    print diff_x
    print diff_y

    for i in range(10):
        fan.leftdownmove(int(start[0]+(i+1)*diff_x),int(start[1]+(i+1)*diff_y))
        # dm.mover(diff_x,diff_y)
        sleep(.01)
    # sleep(1)

def logVictoryLevel(dm,windowName="None"):
    if windowName == "jiangshi":
        return 1
    returnV = 1
    nowDict = dm.getNowDict()
    dm.useDict(0)
    levelSize = (27,20)
    levelPos = [(238,289),(379,289),(521,289),(661,289),(238,358),(379,358)]
    expPos = [(220,318),(361,318),(504,318),(644,318),(220,387),(361,387)]
    tmp = []
    for i in levelPos:
        ret = dm.ocr(i[0],i[1],i[0]+levelSize[0],i[1]+levelSize[1],"f2edda-808080",0.7)
        if ret.isdigit():
            tmp +=[ret]
        else:
            tmp+=['0']
    for (index,i) in enumerate(expPos):
        ret = dm.ocr(i[0],i[1],i[0]+levelSize[0],i[1]+levelSize[1],"ddd8c6-151515|a29b8c-151515|b8b1a1-151515",0.9)
        # if ret!="exp":
        if 'e' not in ret and 'x' not in ret and 'p' not in ret:
            tmp[index]+="(full)"
            print 'full level try end script'
            returnV = 0

    message1 = ",".join(tmp)
    message = windowName +": " + message1
    sendToServer(message)
    dm.useDict(nowDict)
    return returnV

def reg():
    dm = win32com.client.Dispatch('dm.dmsoft')
    print dm.ver()

    hMod = windll.kernel32.GetModuleHandleA('dm1.dll')
    memarray = (c_char*1).from_address(hMod+0x1063D0)
    print memarray[0]
    memarray[0] ='1'
    print memarray[0]
    return dm
    # ret = dm.Reg("xiewei200820088ca5e457a09d6e301df9a582c7fcc74c","1")
    # if ret!=1:
    #     print ret
    #     return 0
    # else:
    #     print 'reg success'
    #     return dm


def moveWindowAndBind(dm,windowName):
    hwnd = dm.FindWindow("",windowName)
    hwndGame = dm.EnumWindow(hwnd,"kaopu","",1+16)
    print hwndGame
    ret = dm.BindWindow(hwndGame, "dx2", "windows", "normal", 0)
    if ret ==1:
        print 'bind OK'

    # dm.MoveWindow(hwnd, -2 , -38)
    # ret = dm.MoveWindow(hwnd, -2 , -38)

    setDict(dm)
    return hwndGame
def setDict(dm):
    rootPath = os.path.abspath('..')
    # dm.SetPath("../")
    dm_ret = dm.SetDict(0, "c:/anjianScript/dict/level.txt")
    dm_ret = dm.SetDict(1, os.path.join(rootPath,u"dict/数字.txt"))
    dm_ret = dm.SetDict(2, os.path.join(rootPath,u"dict/阴阳字库.txt"))
    dm.useDict(1)

def FindPic(dm,x1,y1,x2,y2,picName, delta_color,sim, dir1):
    s = dm.FindPicE(x1, y1, x2, y2, picName, delta_color,sim, dir1)
    ss = s.split('|')
    # print ss[1],ss[2]

    return int(ss[1]),int(ss[2])

def FindMultiPic(dm,x1,y1,x2,y2,picName, delta_color,sim, dir1):
    s = dm.FindPicEx(x1, y1, x2, y2, picName, delta_color,sim, dir1)
    ss = s.split('|')
    # print ss[1],ss[2]
    ret = []
    for i in ss:
        value = i.split(',')
        if len(value)>=3:
            ret.append((int(value[1]),int(value[2])))
    return ret

def sendToServer(message):
    global client
    client.q.put(message)

def send(message):
    global dm_send
    pythoncom.CoInitialize()
    if dm_send == None:
        dm_send = reg()
        send1(dm_send,message)
    else:
        send1(dm_send,message)

def send1(dm,message):
    hwnd = dm.FindWindow("",u"文件传输助手")
    if hwnd == 0:
        return
    ret = dm.BindWindow(hwnd,"dx","dx","windows",0)
    dm.MoveTo(293, 530)
    dm.leftClick()
    sleep(.500)
    dm.KeyPressStr(message,50)

    dm.moveto(510, 564)
    dm.leftClick()
def autoBattle(dm,cf = None,shenLe = False,isRecordLevel = False,windowName = "none",isChangeFood = False):
    fan = Fan(dm,windowName)
    returnV = 1
    intX,intY = FindPic(dm,500,300,570,370,u"C:/anjianScript/阴阳师碎片/协助.bmp","101010", 0.8, 0)
    if intX > 0:
        ensureX,ensureY = intX,intY
        print 'find assist'
        intX,intY = FindPic(dm,409,358,448,383,u"C:/anjianScript/通用经验/协助金币.bmp","202020", 0.75, 0)
        if intX>0:
            fan.leftclick(529,391)
            sleep(.500)
        else:
            fan.leftclick(ensureX,ensureY)
            sleep(.500)

    if shenLe:
        intX,intY = FindPic(dm,18,501,36,523,u"C:/anjianScript/通用经验/战斗指南针.bmp","000000",0.8,0)
        if intX>0:
            fan.leftclick(intX,intY)
            sleep(3)

        intX,intY = FindPic(dm,17,553,55,572,u"C:/anjianScript/通用经验/手动.bmp","000000",0.8,0)
        if intX>0:
            sleep(.100)
            zhaoyuX,zhaoyuY = FindPic(dm,669,553,702,579,u"C:/anjianScript/通用经验/招鱼.bmp","000000",1,0)
            if zhaoyuX>0:
                fan.leftclick(zhaoyuX,zhaoyuY)
                sleep(.700)
                fan.leftclick(365,274)
                sleep(.300)
                fan.leftclick(365,274)
                sleep(.300)
                fan.leftclick(365,274)
                sleep(.300)
            elif dm.cmpColor(602,541,"b47d30-101010",1)==0:#自动手动切换
                fan.leftclick(intX,intY)
                sleep(.300)
                fan.leftclick(intX,intY)
                sleep(.300)
            return 2

        intX,intY = FindPic(dm,13,549,60,584,u"C:/anjianScript/通用经验/自动.bmp","000000",0.8,0)
        if intX>0:
            fan.leftclick(intX,intY)
            sleep(.500)
            return 2



    intX,intY = FindPic(dm,682,556,777,587,u"C:/anjianScript/公会突破/鼓下.bmp","000000",0.8,0)
    if intX>0:
        if isChangeFood:
            cf = ChangeFood(dm,windowName)
            cf.startChange()
        else:
            fan.leftclick(724,500)
            sleep(.500)

    intX,intY = FindPic(dm,256,85,326,139,u"C:/anjianScript/阴阳师碎片/失败鼓.bmp","000000",0.8,0)
    if intX>0:
        fan.leftclick(intX,intY)
        sleep(.500)

    intX,intY = FindPic(dm,227,46,385,190,u"C:/anjianScript/阴阳师碎片/胜利鼓.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:

        if isRecordLevel:
            sleep(2.5)
            returnV = logVictoryLevel(dm,windowName)

        if returnV!=0 or windowName == "jiangshi":
            fan.leftclick(307, 121)
            sleep(.500)

    intX,intY = FindPic(dm,290, 191,496, 395,u"C:/anjianScript/阴阳师碎片/胜利佛1.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        if cf is not None:
            cf.needRecord = True
        fan.leftclick(307, 121)
        sleep(.500)
    intX,intY = FindPic(dm,350, 390,434, 449,u"C:/anjianScript/阴阳师碎片/胜利碗.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        fan.leftclick(307, 121)
        sleep(.500)
    intX,intY = FindPic(dm,290, 332,356, 356,u"C:/anjianScript/阴阳师碎片/我很忙.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        fan.leftclick(intX, intY)
        sleep(.500)
    return returnV

def logEnergy(dm,cf,windowName):

    sInt = 100
    dm.usedict(1)
    s = dm.Ocr(605, 4, 633, 31, "e4ddca-505050", 0.7)
    if len(s)<0:
        return
    if s.isdigit():
        sInt = int(s)
        print windowName +":"+ s
        message = str(datetime.datetime.now())[11:18] +"|"+windowName+": "+str(sInt)
        # f = open("c:/"+windowName+".txt",'a')
        # print >>f,message
        sendToServer(message)
    # if sInt < cf.aimEnergy:
    #     cf.gameOver = True
