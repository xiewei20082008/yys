from socket import *

host = '172.246.84.119'
tcpPort = 21568
bufsize = 2000
# tcp
tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.connect((host,tcpPort))
print 'here'

# dm = reg()
# hwnd = moveWindowAndBind(dm,'xiaohao')
# fan = Fan(hwnd)
# try:
#     while True:
#         # dm.moveto(185,198)
#         print 'here'
#         fan.leftclick(185,198)
#         sleep(2)
#         # dm.moveto(185,307)
#         fan.leftclick(185,307)
#         sleep(2)
#         # dm.moveto(185,420)
#         fan.leftclick(185,420)
#         sleep(2)
# except KeyboardInterrupt as e:
#     print e
#     dm.UnBindWindow()
