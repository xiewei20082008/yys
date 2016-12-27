#coding=utf8
import win32com.client
from time import sleep
import os
import datetime
import pythoncom
import Client
import threading
from ctypes import *

dm_send = None

client = Client.Client()
t_client = threading.Thread(target = client.send)
t_client.start()

def dragMoveTo(dm,start,end):
    sleep(.500)
    times = 10.0
    diff_x = (end[0]-start[0])/times
    diff_y = (end[1]-start[1])/times
    print diff_x
    print diff_y

    for i in range(10):
        dm.mover(diff_x,diff_y)
        sleep(.01)
    sleep(1)

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
        if ret!="exp":
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

    hMod = windll.kernel32.GetModuleHandleA('dm.dll')
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
def autoBattle(dm,cf = None,shenLe = False,isRecordLevel = False,windowName = "none"):
    returnV = 1
    intX,intY = FindPic(dm,500,300,570,370,u"C:/anjianScript/阴阳师碎片/协助.bmp","101010", 0.8, 0)
    if intX > 0:
        ensureX,ensureY = intX,intY
        print 'find assist'
        intX,intY = FindPic(dm,409,358,448,383,u"C:/anjianScript/通用经验/协助金币.bmp","202020", 0.75, 0)
        if intX>0:
            dm.moveto(529,391)
            dm.leftClick()
            sleep(.500)
        else:
            dm.moveto(ensureX, ensureY)
            dm.leftclick()
            sleep(.500)
    if shenLe:
        intX,intY = FindPic(dm,18,501,36,523,u"C:/anjianScript/通用经验/战斗指南针.bmp","000000",0.8,0)
        if intX>0:
            dm.moveto(intX,intY)
            dm.leftclick()
            sleep(3)

        intX,intY = FindPic(dm,17,553,55,572,u"C:/anjianScript/通用经验/手动.bmp","000000",0.8,0)
        if intX>0:
            sleep(.100)
            zhaoyuX,zhaoyuY = FindPic(dm,669,553,702,579,u"C:/anjianScript/通用经验/招鱼.bmp","000000",1,0)
            if zhaoyuX>0:
                dm.moveto(zhaoyuX,zhaoyuY)
                dm.leftclick()
                sleep(.700)
                dm.moveto(416,282)
                dm.leftclick()
                sleep(.300)
            elif dm.cmpColor(602,541,"b47d30-101010",1)==0:#自动手动切换
                dm.moveto(intX,intY)
                dm.leftclick()
                sleep(.300)
                dm.leftclick()
                sleep(.300)
            return 2

        intX,intY = FindPic(dm,13,549,60,584,u"C:/anjianScript/通用经验/自动.bmp","000000",0.8,0)
        if intX>0:
            dm.moveto(intX,intY)
            dm.leftclick()
            sleep(.500)
            return 2



    intX,intY = FindPic(dm,682,556,777,587,u"C:/anjianScript/公会突破/鼓下.bmp","000000",0.8,0)
    if intX>0:
        dm.moveto(724,500)
        dm.leftclick()
        sleep(.500)

    intX,intY = FindPic(dm,256,85,326,139,u"C:/anjianScript/阴阳师碎片/失败鼓.bmp","000000",0.8,0)
    if intX>0:
        dm.moveto(intX,intY)
        dm.leftclick()
        sleep(.500)

    intX,intY = FindPic(dm,227,46,385,190,u"C:/anjianScript/阴阳师碎片/胜利鼓.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:

        if isRecordLevel:
            sleep(2.5)
            returnV = logVictoryLevel(dm,windowName)

        if returnV!=0 or windowName == "jiangshi":
            dm.moveto(307, 121)
            dm.leftclick()
            sleep(.500)

    intX,intY = FindPic(dm,290, 191,496, 395,u"C:/anjianScript/阴阳师碎片/胜利佛1.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        if cf is not None:
            cf.needRecord = True
        dm.moveto(307, 121)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,350, 390,434, 449,u"C:/anjianScript/阴阳师碎片/胜利碗.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        dm.moveto(307, 121)
        dm.leftclick()
        sleep(.500)
    intX,intY = FindPic(dm,290, 332,356, 356,u"C:/anjianScript/阴阳师碎片/我很忙.bmp","000000", 0.9, 0)
    if intX > 0 and intY > 0:
        dm.moveto(intX, intY)
        dm.leftclick()
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
