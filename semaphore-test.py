import threading
import time
import random

semaphore = threading.Semaphore(0)  # 创建信号量


def producer():
    global item
    time.sleep(3)
    item = random.randint(1, 1000)
    print("product : 生产 %s." % item)
    semaphore.release()


def consumer():
    print("consumer : 挂起")
    semaphore.acquire()
    print("consumer : 消费 %s." % item)


threads = []

for i in range(0, 2):
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

for t in threads:
    t.join()
