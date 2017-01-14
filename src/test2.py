
from socket import *

host = '127.0.0.1'
tcpPort = 21568
bufsize = 2000
# tcp
tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.bind((host,tcpPort))
tcpSock.listen(1)
conn,addr = tcpSock.accept()
print 'here'
