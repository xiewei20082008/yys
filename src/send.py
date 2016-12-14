from time import sleep


try:
    a = 10/0
except KeyboardInterrupt as e:
    print e
    print 'find'
except Exception as e:
    print e
    print 'other'
