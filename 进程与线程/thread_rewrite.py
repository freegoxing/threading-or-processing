
""""
重写thread，定义新方法
"""
import threading
class MyThread(threading.Thread):
    def run(self):
        print(self._args)

t = MyThread(args='hello')
t.start()
