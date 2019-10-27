"""
用类定义装饰器
"""
import time


class Decorator:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        start_time = time.clock()
        self._func(*args)
        end_time = time.clock()
        print("函数执行时间" + str(end_time - start_time))


@Decorator
def add(*args):
    print(sum(args))


"""此处将add变成了Decorator(add)"""

add(1, 2, 3, 4)
