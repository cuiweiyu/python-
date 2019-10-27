"""
装饰器的参数传递(二)：多个装饰器
（1）使用装饰器a时，会调用上面的a函数
（2）装饰：先A 后B
（3）调用执行：先bbbb后aaaaa : 这是因为每次装饰之后都会生成一个新的函数。函数的执行是层层向上层调用。

"""


def a(func):
    print("执行了装饰器a")

    def In():
        print("aaaaaa")
        func()

    return In


def b(func):
    print("执行了装饰器b")

    def In():
        print("bbbb")
        func()

    return In


@b
@a
def pr():
    print("pr 函数")


pr()
