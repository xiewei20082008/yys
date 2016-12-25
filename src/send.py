#coding=utf8
from time import sleep
import threading

import win32com.client
usedll=win32com.client.Dispatch("QMDispatch.QMFunction")
print usedll
ret = 0
ret = usedll.FindBmpPic("d:/N.bmp",0,0,1024,768, "d:/N.bmp",  0, 1.0)
print ret
