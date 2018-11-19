import threading
import time

g_num = 1
lock = threading.RLock()


def handle(sid):
    lock.acquire()
    global g_num
    g_num *= 2
    time.sleep(sid % 2)
    print("thread", sid, ":", g_num)
    lock.release()


threads = []
for i in range(1, 11):
    t = threading.Thread(target=handle, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('main thread end')
