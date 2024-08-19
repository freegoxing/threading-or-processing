import threading
class Fun:
    instance = None
    lock = threading.RLock()

    def __init__(self, name):
        self.name = name


    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            cls.instance = object.__new__(cls)
            return cls.instance