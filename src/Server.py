from socket import *
from time import sleep
import os
class Server:
    def __init__(self):
        self.host = '172.246.84.119'
        self.port = 21567
        self.bufsize = 1024
        addr = (self.host,self.port)
        self.udpSerSock = socket(AF_INET, SOCK_DGRAM)
        self.udpSerSock.bind(addr)
    def handlePhone(self,message,addr):
        if message == "readLog":
            print 'command readLog'
            ret = os.popen('tail -n 20 /root/log.txt')
            self.udpSerSock.sendto(ret.read(),addr)
        if message == "delLog":
            ret = os.popen('rm -f /root/log.txt')
            self.udpSerSock.sendto(ret.read(),addr)

    def open(self):
        while True:
            print 'waiting for message...'
            data, addr = self.udpSerSock.recvfrom(self.bufsize)
            file = open('/root/log.txt','a')
            message = data.split('~')
            if len(message)>1:
                if message[0]=='1':
                    self.handlePhone(message[1],addr)
                elif message[1] == 'heartbeat':
                    print 'receive heartbeat'
                    self.udpSerSock.sendto(message[0],addr)
                else:
                    print >>file,message[1]
                    self.udpSerSock.sendto(message[0],addr)
            file.close()
    def close(self):
        self.udpSerSock.close()

server = Server()
server.open()
