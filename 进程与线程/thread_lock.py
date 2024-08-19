from threading import Thread, RLock

number = 0
loop = 1000000
look = RLock()

def add1(loop):                             #def add1(loop):
    global number                           #    global number
    look.acquire()                          #    with look:
    for i in range(loop):                   #        for i in range(loop):
        number += 1                         #          number += 1
    look.release()


def sub1(loop):
    global number
    look.acquire()
    for i in range(loop):
        number -= 1
    look.release()

thread1 = Thread(target=add1, args=(loop,))
thread2 = Thread(target=sub1, args=(loop,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(number)