import threading
import queue
import random
import time


def produce(q):
    i = 0
    while i<10:
        num = random.randint(1,100)
        q.put('生产者生产数据:%d'%num)
        print('生产者产生数据：%d'%num)
        time.sleep(1)
        i += 1
    q.put(None)
    #完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到：%s'%item)
        time.sleep(4)

    q.task_done()


if __name__ == '__main__':
    q =queue.Queue(10)
    arr = []

    #创建生产者
    th = threading.Thread(target=produce,args=(q,))
    th.start()

    #创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    th.join()
    tc.join()
    print('end')