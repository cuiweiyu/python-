import time
"""
嵌套函数 定义的装饰器
类  定义的装饰器
"""

def cal_time(fun):
    def ln():
        start_time = time.clock()
        res = fun()
        end_time = time.clock()
        print("函数调用时间：" + str(end_time - start_time))
        if res is not None:
            print("成功")
        else:
            print("成功")

    return ln


@cal_time
def a():
    temp = []
    for i in range(100000):
        temp.append("LPL")
    print(len(temp))


# print(cal_time(a))
# new_func = cal_time(a)
# new_func()

a()
# 装饰器：在不改变函数内部代码的情况下增添一些新的功能
