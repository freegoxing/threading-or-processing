# import time
# start = time.time()
# result = 0
# for i in range(100000000):
#     result += i
# print(result)
# end = time.time()
# consume = format(end - start, '.2f')
# print(consume)


import time
import multiprocessing
def task(start, end, quene):
    result = 0
    for i in range(start, end):
        result += i
    quene.put(result)


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    start = time.time()

    p1 = multiprocessing.Process(target=task, args=(0, 25000000, queue))
    p1.start()

    p2 = multiprocessing.Process(target=task, args=(25000000, 50000000, queue))
    p2.start()

    p3 = multiprocessing.Process(target=task, args=(50000000, 75000000, queue))
    p3.start()

    p4 = multiprocessing.Process(target=task, args=(75000000, 50000000, queue))
    p4.start()

    v1 = queue.get()
    v2 = queue.get()
    v3 = queue.get()
    v4= queue.get()
    print(v1 + v2 + v3 + v4)

    end = time.time()

    consume = format(end - start, '.2f')
    print(consume)