import logging


def use_logging(func):
    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()

    return wrapper


@use_logging
def foo():
    print('i am foo')


@use_logging
def heh():
    a = 0
    b = 9
    return a + b


# 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()
ab = heh()
print(ab)
# use_logging 就是一个装饰器，它一个普通的函数，它把执行真正业务逻辑的函数 func 包裹在其中，看起来像 foo 被 use_logging 装饰了一样，use_logging 返回的也是一个函数，这个函数的名字叫 wrapper。在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。
