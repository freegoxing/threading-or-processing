"""
pip install greenlet
利用greenlet
"""
from greenlet import greenlet as g

def fun1():
    print(1)
    g2.switch()
    print(2)
    g2.switch()


def fun2():
    print(3)
    g1.switch()
    print(4)

g1 = g(fun1)
g2 = g(fun2)
g1.switch()

"""
用yield
"""
