import logging
import time

"""
装饰器的参数传递(二)：装饰器中添加参数@out(3)
  被修饰函数的参数，对应内层函数的参数
  被修饰函数的指针，对应外层函数的参数
"""


def out(a):
    print("最外层函数的参数：", a)

    def cal_time(func):
        print("中间层函数的参数：", func)

        def In(*args):
            print("最里层函数的参数：", func)
            start_time = time.clock()
            func(*args)
            end_time = time.clock()
            tt = end_time - start_time
            logging.warn("Func %s Time %s " % (func.__name__, tt))
            # return func()  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()

        return In

    return cal_time


@out(3)
def add_all(*args):
    print(sum(args))


add_all(1, 2)
