#coding=utf8
from time import sleep
import threading


while True:
    try:
        sleep(20)
    except KeyboardInterrupt:
        print 'end'
        break
