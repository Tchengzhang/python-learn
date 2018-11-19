from multiprocessing import Process
import time
import random

import os


# 使用继承的方式实现进程
class mypro(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("%s start " % self.name, os.getpid())
        time.sleep(random.randint(1, 3))
        print("%s end " % self.name, os.getpid())


if __name__ == '__main__':
    p1 = mypro("test")
    p1.start()
    print("主进程！", os.getpid())
    p1.join()
    print("主进程结束。")
