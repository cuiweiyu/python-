"""
如果不做任何处理， callable
（1）函数可以调用
（2）类可调用
（3）类的实例对象不可调用：类的__call__ 这个方法可以让实例对象变得可以调用
"""


def main():
    print("你好，我是旗子")


print("函数", callable(main))


class B:
    pass


class Ba:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


print("类", callable(B))
print("实例对象", callable(B()))
b = B()
print("实例对象b", callable(b))
ba = Ba()
print("实例对象ba", callable(ba()))
