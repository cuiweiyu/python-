import logging
import time

"""
装饰器的参数传递(一)
  被修饰函数的参数，对应内层函数的参数
  被修饰函数的指针，对应外层函数的参数
"""


def cal_time(func):
    def In(name):
        start_time = time.clock()
        func(name)
        end_time = time.clock()
        tt = end_time - start_time
        logging.warn("Func %s Time %s " % (func.__name__, tt))
        # return func()  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()

    return In


@cal_time
def who(name):
    print('i am ' + name)


# @cal_time
# def heh():
#     a = 0
#     b = 9
#     return a + b


# 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
who("cwy")
# ab = heh()
# print(ab)
# use_logging 就是一个装饰器，它一个普通的函数，它把执行真正业务逻辑的函数 func 包裹在其中，看起来像 foo 被 use_logging 装饰了一样，use_logging 返回的也是一个函数，这个函数的名字叫 wrapper。在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。
