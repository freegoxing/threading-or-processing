from multiprocessing import Process as c
import time

def task():
    print('start')
    time.sleep(2)
    print('end')


if __name__ == '__main__':
    p1 = c(target=task)
    p1.daemon = True
    print('a')
    p1.start()
    print('b')

