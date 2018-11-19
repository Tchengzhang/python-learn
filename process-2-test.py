from multiprocessing import Process
import time
import random

import os


# 使用类的实例化创建进程
def run_proc(name):
    print("%s start " % name, os.getpid())
    time.sleep(random.randint(1, 3))
    print("%s end " % name, os.getpid())


if __name__ == '__main__':
    p1 = Process(target=run_proc, args=("test",))
    print("主进程！", os.getpid())
    p1.start()
    p1.join()
    print("主进程结束")
