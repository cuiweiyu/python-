def add(x, y):
    print(x + y)


# 闭包 = 函数块 + 创建它时的环境
# 当（内层函数）调用了（外层函数）作用域中的“变量”时。外层函数调用结束后，将会把内层函数涉及到的变量“送”给内层函数以保证其正常运行
def temp1(x, y):
    def add():
        print(x + y)
    return add  # 函数名当做返回值(返回函数指针)


add(1, 2)
b = add
print(b)
b(2, 2)
print(b is add)  #

# 函数名当做返回值
print("temp1(2, 3)")
print(temp1(2, 3))
print("temp1(2, 3)()")
temp1(2, 3)()
