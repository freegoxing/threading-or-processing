"""
与C有关的Value， Arry
Manger
上面为不常用
"""

"""
第一Queen
"""
# from multiprocessing import Process, Queue
#
# def task(q):
#     for i in range(10):
#         q.put(i)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=task, args=(q,))
#     p.start()
#
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     print(q.get())
"""
第二Pipes
"""
from multiprocessing import Process, Pipe


