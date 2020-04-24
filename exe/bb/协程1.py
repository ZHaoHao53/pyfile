import time
from greenlet import greenlet

def a():
    for i in range(5):
        print('a'+str(i))
        gb.switch()
        time.sleep(1)


def b():
    for i in range(5):
        print('b'+str(i))
        gc.switch()
        time.sleep(1)


def c():
    for i in range(5):
        print('c'+str(i))
        ga.switch()
        time.sleep(1)


if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)


    ga.switch()
    gb.switch()
    gc.switch()