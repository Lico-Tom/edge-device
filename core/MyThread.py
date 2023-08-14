import threading


class Thread(threading.Thread):
    def __init__(self, fun):
        threading.Thread.__init__(self)  # 重写父类方法
        self.fun = fun

    def run(self):
        self.fun
