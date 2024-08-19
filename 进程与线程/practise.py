import threading
from concurrent.futures import ThreadPoolExecutor

def task():
    num_list = [int(i.split(',')[-1]) for i in file_list]
    result = sum(num_list)
    print(result)


def read_file(file_name):
    file = open('text.txt', 'r')
    file.readline()
    file_list = []
    for line in file:
        file_list.append(line.strip())
        if len(file_list) == 100:
            pool.submit(task, file_list)
            file_list = []
    if file_list:
        pool.submit(task, file_list)

pool = ThreadPoolExecutor(max_workers=10)

if __name__ == '__main__':
    run()




