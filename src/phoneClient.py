from socket import *
import time
from time import sleep

class Client:
    def __init__(self):
        self.host = '172.246.84.119'
        self.port = 21567
        self.bufsize = 1024
        self.udpCliSock = socket(AF_INET, SOCK_DGRAM)
        self.addr = (self.host,self.port)
        print 'socket ok'
        self.udpCliSock.settimeout(5)
    def send(self,message):
        data = '1~'+message
        self.udpCliSock.sendto(data,self.addr)
        try:
            ret,tmp = self.udpCliSock.recvfrom(self.bufsize)
            print ret
        except:
            print 'receive time out'

    def close(self):
        self.udpCliSock.close()

client = Client()
# client.send('delLog')
client.send('readLog')
