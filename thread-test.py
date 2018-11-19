import threading


def handle(sid):
    print("Thread %d run" % sid, threading.current_thread())


# for i in range(1, 11):
#     t = threading.Thread(target=handle, args=(i,))
#     t.start()
# print("main thread", threading.current_thread())

class MyThread(threading.Thread):
    def __init__(self, sid):
        self.sid = sid
        threading.Thread.__init__(self)

    def run(self):
        handle(self.sid)


for i in range(1, 11):
    t = MyThread(i)
    t.start();
