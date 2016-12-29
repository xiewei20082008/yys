from toolkit import *
dm = reg()
hwnd = moveWindowAndBind(dm,'xiaohao')
fan = Fan(hwnd)
try:
    while True:
        # dm.moveto(185,198)
        print 'here'
        fan.leftclick(185,198)
        sleep(2)
        # dm.moveto(185,307)
        fan.leftclick(185,307)
        sleep(2)
        # dm.moveto(185,420)
        fan.leftclick(185,420)
        sleep(2)
except KeyboardInterrupt as e:
    print e
    dm.UnBindWindow()
