""""
setDaemon 设置守护线程，主线程结束，子线程结束
"""
import threading, time
def task(interval):
    print("start thread_son task")
    time.sleep(interval)
    print("end thread_son task")


thread = threading.Thread(target=task, args=(3000,))
thread.setDaemon(True)
thread.start()
print("end thread_main task")