import ExpElf
from toolkit import *
import threading
from time import sleep
import sys
import os

dm = reg()



def main():
    global dm
    print dm
    # dm.SetMouseDelay("windows",150)
    # cf = ExpElf.ExpElf(dm,"jiangshi",4,0,isRush = False,shenLe = False)
    cf = ExpElf.ExpElf(dm,"dahao",11,10,isRush = True,isDelayRush = False,shenLe = True)
    # cf = ExpElf.ExpElf(dm,"xiaohao",11,10,isRush = True,isDelayRush = False,shenLe = True)
    cf.runUp()
    print 'thread end'


t1 = threading.Thread(target = main)
t1.start()

s1 = raw_input()
dm.UnBindWindow()
print "end script"
os._exit(0)
