from socket import *
from time import sleep
import os
import time
import threading
class Server:
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 21567
        self.tcpPort = 21568
        self.bufsize = 1024
        addr = (self.host,self.port)
        self.udpSerSock = socket(AF_INET, SOCK_DGRAM)
        self.udpSerSock.bind(addr)
        # TCP
        self.tcpSock = socket(AF_INET, SOCK_STREAM)
        self.tcpSock.bind((gethostname(),self.tcpPort))
        self.tcpSock.listen(5)


        self.command = {}
    def tcpHandle(self):
        print 'here is tcp start'
        print 'here is aft listen'
        conn,addr = self.tcpSock.accept()
        print 'Connection address:', addr
        while True:
            message = conn.recv(self.bufsize)
            print message
            if message == "readLog":
                print 'tcp command readLog'
                ret = os.popen('tail -n 20 /root/log.txt')
                returnMessage = ret.read()
                conn.send(returnMessage)
    def handlePhone(self,message,conn):
        if message == "readLog":
            print 'command readLog'
            ret = os.popen('tail -n 20 /root/log.txt')
            returnMessage = ret.read()
            conn.send(returnMessage)
            # self.udpSerSock.sendto(returnMessage,addr)
        elif message == "delLog":
            ret = os.popen('rm -f /root/log.txt')
            returnMessage = ret.read()
            conn.send(returnMessage)
                # self.udpSerSock.sendto(returnMessage,addr)
        elif message.startswith('sendCmd:'):
            txt = message.split(':')
            if len(txt)>1 and txt[1] not in self.command.values():
                txt = txt[1]
                nowTime = str(time.time())
                self.command[nowTime] = txt
            conn.send('command received')
            # self.udpSerSock.sendto('command received',addr)

    def open(self):
        def solveHeartbeat(message,conn):
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
                conn.send(reply)
                # self.udpSerSock.sendto(reply,addr)
                return True

            # self.udpSerSock.sendto('ok',addr)
            conn.send('ok')
        while True:
            print 'waiting for message...'
            conn, addr = self.tcpSock.accept()
            conn.settimeout(10)
            try:
                data = conn.recv(self.bufsize)
                file = open('/root/log.txt','a')
                message = data.split('~')
                if len(message)>1:
                    if message[0]=='1':
                        self.handlePhone(message[1],conn)
                    elif message[1] == 'heartbeat':
                        print 'receive heartbeat'
                        solveHeartbeat(message,conn)
                    else:
                        print >>file,message[1]
                        conn.send(message[0])
                        # self.udpSerSock.sendto(message[0],addr)
                file.close()
            except:
                continue
            conn.close()
    def close(self):
        self.udpSerSock.close()

server = Server()
server.open()
# t1 = threading.Thread(target = server.open)
# t2 = threading.Thread(target = server.tcpHandle)
# t2.start()
# t1.start()
# try:
#     sleep(20)
# except:
#     print 'end'
#     os._exit(0)
