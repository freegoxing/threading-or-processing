


"""
线程池
"""
# import time
# from concurrent.futures import ThreadPoolExecutor
# import threading
#
# lock = threading.Lock()
#
# pool = ThreadPoolExecutor(10)
#
# url_list = ['www.{}.com'.format(i) for i in range(50)]
#
# def task(url, interval):
#     # with lock:
#         print('start' + url)
#         time.sleep(interval)
#         print('end')
#
# for url in url_list:
#      pool.submit(task, url, 1.5)
#
# pool.shutdown()
# print('End')

"""
线程池
多任务时，用
future = pool.submit()
future.add_done_callback等来连续任务
"""

# import time
# from concurrent.futures import ThreadPoolExecutor
# import threading
# import random
#
# def task(url, interval):
#     print('task' + url + 'start')
#     time.sleep(interval)
#     return random.randint(1, 10)
#
#
# def done(response):
#     print('result', response.result)
#
#
# pool = ThreadPoolExecutor(10)
#
# url_list = ['www.{}.com'.format(i) for i in range(20)]
#
# for url in url_list:
#     future = pool.submit(task, url, 1.5)
#     future.add_done_callback(done)


import time
from concurrent.futures import ThreadPoolExecutor
import threading
import random

def task(video_url):
    print('task', video_url)
    time.sleep(1)
    return random.randint(1, 10)


pool = ThreadPoolExecutor(10)

future_list = []

url_list = ['www.xxx-{}.com'.format(i) for i in range(15)]

for url in url_list:
    fur = pool.submit(task, url)
    future_list.append(fur)

pool.shutdown()

for future in future_list:
    print(fur.result())