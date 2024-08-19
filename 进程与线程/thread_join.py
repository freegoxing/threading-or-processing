# import threading
#
# loop = 1000000
# number = 0
# def add_(loop):
#     global number
#     for i in range(loop):
#         number += 1
#
#
# thread1 = threading.Thread(target=add_, args=(loop,))
# thread1.start()
#
# print(number)


"""
join 等待子线程执行完毕，继续主线程
"""



# import threading
#
# loop = 1000000
# number = 0
# def add_(loop):
#     global number
#     for i in range(loop):
#         number += 1
#
#
# thread1 = threading.Thread(target=add_, args=(loop,))
# thread1.start()
# thread1.join()
# print(number)


"""
在多线程中，子线程会相互切换
不用（R）Lock，就用
thread1.start
thread1.join()

thread2.start
thread2.join()
"""


# import threading
# number = 0
# loop = 1000000
# def add1(loop):
#     global number
#     for i in range(loop):
#         number += 1
#
#
# def sub1(loop):
#     global number
#     for i in range(loop):
#         number -= 1
#
# thread1 = threading.Thread(target=add1, args=(loop,))
# thread2 = threading.Thread(target=sub1, args=(loop,))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(number)
#





# import threading
# number = 0
# def add1():
#     global number
#     for i in range(1000000):
#         number += 1
#
#
# def sub1():
#     global number
#     for i in range(1000000):
#         number -= 1
#
# thread1 = threading.Thread(target=add1)
# thread2 = threading.Thread(target=sub1)
#
# thread1.start()
# thread1.join()
#
# thread2.start()
# thread2.join()
#
# print(number)