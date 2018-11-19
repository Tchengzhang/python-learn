import threading
import time


# 定时器的调用
# def timer_handle():
#     print("你好，定时器")
#
#
# timer = threading.Timer(2, timer_handle)
# timer.start()

# 循环定时器
def loop_timer_handle():
    print("你好，定时器")
    global timer2
    timer2 = threading.Timer(2, loop_timer_handle)
    timer2.start()


timer2 = threading.Timer(2, loop_timer_handle)
timer2.start()
time.sleep(10)
timer2.cancel()
