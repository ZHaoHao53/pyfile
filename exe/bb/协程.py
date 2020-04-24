import time


def task1():
    for i in range(3):
        print('a'+str(i))
        yield
        time.sleep(1)

def task2():
    for i in range(3):
        print('b'+str(i))
        yield
        time.sleep(2)

if __name__ == '__main__':
    g1 = task1()
    g2 = task2()


    while True:
        try:
            next(g1)
            next(g2)

        except:
            break