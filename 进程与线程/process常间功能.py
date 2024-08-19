import multiprocessing
import threading
import time
import os

def task():
    print('start')
    print('子线程', os.getpid(), '父线程', os.getppid())
    print('线程个数', len(threading.enumerate()))
    time.sleep(2)
    print(p1.name)

if __name__ == '__main__':
    print(os.getpid())
    p1 = multiprocessing.Process(target=task, name='free')
    p1.start()
print(multiprocessing.cpu_count()) # 获取cpu个数