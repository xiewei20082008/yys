from socket import *
from time import sleep
import os
import time
class Server:
    def __init__(self):
        self.host = '172.246.84.119'
        self.port = 21567
        self.bufsize = 1024
        addr = (self.host,self.port)
        self.udpSerSock = socket(AF_INET, SOCK_DGRAM)
        self.udpSerSock.bind(addr)
        self.command = {}
    def handlePhone(self,message,addr):
        if message == "readLog":
            print 'command readLog'
            ret = os.popen('tail -n 20 /root/log.txt')
            self.udpSerSock.sendto(ret.read(),addr)
        elif message == "delLog":
            ret = os.popen('rm -f /root/log.txt')
            self.udpSerSock.sendto(ret.read(),addr)
        elif message.startswith('sendCmd:'):
            txt = message.split(':')
            if len(txt)>1 and txt[1] not in self.command.values():
                txt = txt[1]
                nowTime = str(time.time())
                self.command[nowTime] = txt
            self.udpSerSock.sendto('command received',addr)

    def open(self):
        def solveHeartbeat(message,addr):
            #test
            print 'heartbeat print dict:'
            for k,v in self.command.items():
                print k,v
            #
            if message[2]:
                if self.command.has_key(message[2]):
                    print 'del'+ str(self.command[message[2]])
                    del self.command[message[2]]
            for k,v in self.command.items():
                reply = '~'.join([message[0],k,v])
                self.udpSerSock.sendto(reply,addr)
                return True

            self.udpSerSock.sendto('ok',addr)
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
                    solveHeartbeat(message,addr)
                else:
                    print >>file,message[1]
                    self.udpSerSock.sendto(message[0],addr)
            file.close()
    def close(self):
        self.udpSerSock.close()

server = Server()
server.open()
