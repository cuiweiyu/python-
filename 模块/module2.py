from 模块 import module1

print(module1.m1)
print("============")
a = 9
print(a)


def test():
    global a
    a = 0
    # print(a)


print(a)
test()
print(a)

print("============")


def tet():
    ll = 11

    def hh():
        nonlocal ll
        ll = 9
    hh()
    print(ll)


tet()
