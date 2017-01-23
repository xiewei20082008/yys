#coding=utf8
from toolkit import *
import msvcrt

dm = reg()
moveWindowAndBind(dm,'dahao')
fan  = Fan(dm,'dahao')

def moveToBottom():
    for i in range(10):
        fan.leftdown(184,412)
        fan.leftdownmove(184,140)
        fan.leftup(184,140)
def moveToTop():
    for i in range(10):
        fan.leftdown(184,145)
        fan.leftdownmove(184,400)
        fan.leftup(184,400)
def conbine():
    fan.leftclick(209,165)
    sleep(.100)
    fan.leftclick(203,255)
    sleep(.100)
    fan.leftclick(209,346)
    sleep(.100)
    fan.leftclick(519,444)
    sleep(.300)


while True:
    a = msvcrt.getch()
    print a
    if a=='s':
        print 's down'
        break
    elif a=='w':
        moveToBottom()
    elif a == 'q':
        moveToTop()
    elif a == 'e':
        conbine()
dm.UnBindWindow()
