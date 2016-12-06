from socket import *
import time
from Queue import Queue
import threading
from time import sleep

class Client:
    def __init__(self):
        self.q = Queue()
        self.host = '172.246.84.119'
        self.port = 21567
        self.bufsize = 1024
        self.udpCliSock = socket(AF_INET, SOCK_DGRAM)
        self.addr = (self.host,self.port)
        print 'socket ok'
        self.udpCliSock.settimeout(10)
    def send(self):
        while True:
            s = self.q.get()
            nowTime = str(time.time())
            timeData = nowTime+"~"+s
            self.udpCliSock.sendto(timeData,self.addr)
            print 'try send'
            try:
                data,tmp = self.udpCliSock.recvfrom(self.bufsize)
                if data == nowTime:
                    print 'send ok'
                else:
                    print 'receive wrong thing'
                    self.q.put(s)
            except:
                print 'receive time out'
                if("(full)" in s):
                    self.q.put(s)
                continue
            sleep(5)

    def close(self):
        self.udpCliSock.close()
