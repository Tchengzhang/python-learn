import threading
import time
import random

c = threading.Condition()

itemNum = 0
item = 0


def consumer():
    global item
    global itemNum
    c.acquire()
    while 0 == itemNum:
        print("consumer : 挂起.")
        c.wait()
    itemNum -= 1
    print("consumer : 消费%s" % item, itemNum)
    c.release()


def producer():
    global item
    global itemNum
    time.sleep(3)
    c.acquire()
    item = random.randint(1, 1000)
    itemNum += 1
    print("producer : 生产%s" % item)
    c.notifyAll()
    c.release()


threads = []

for i in range(0, 2):
    t1 = threading.Thread(target=consumer)
    t2 = threading.Thread(target=producer)
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

for t in threads:
    t.join()
