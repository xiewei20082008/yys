#coding=utf8
from time import sleep
import threading
from toolkit import *
import pythoncom
from ctypes import *
import ctypes

dm = win32com.client.Dispatch('dm.dmsoft')
print dm.ver()
hMod = windll.kernel32.GetModuleHandleA('dm.dll')
print hMod
# memarray = (ctypes.c_char*1).from_address(hMod+0x1063D0)
# print memarray[0]
# memarray[0] ='1'
# print memarray[0]
# memfield = 1
# print memfield
# print '%x' % hMod
while True:
    # ret = dm.SetWordGap(3)
    print dm.ver()
    # print ret
    sleep(3)
