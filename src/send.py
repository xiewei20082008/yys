from time import sleep
import threading


def tt():
    while True:
        print 'a'
        sleep(1)

t = threading.Thread(target = tt)
t.start()
sleep(2)
