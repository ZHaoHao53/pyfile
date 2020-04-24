import time
import gevent
from gevent import monkey

monkey.patch_all()
#from greenlet import greenlet

def a():
    for i in range(5):
        print('a'+str(i))
        time.sleep(1)


def b():
    for i in range(5):
        print('b'+str(i))
        time.sleep(1)


def c():
    for i in range(5):
        print('c'+str(i))
        time.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)


    g1.join()
    g2.join()
    g3.join()