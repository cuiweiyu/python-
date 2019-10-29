"""
类变量，实例变量，局部变量
类方法，实例方法，静态方法
：：实例方法只能用实例对象调用
    其他两个方法，类和对象都能调用
"""


class Hero():
    # 类变量
    game = "英雄联盟"

    def __init__(self, name):
        # 实例变量
        self.name = name

    # 实例方法
    def flash(self):
        print("我闪-------")
        print(self.game)  # 在实例方法内可以用self调用实例变量
        print(Hero.game)  # 在实例方法内也可用类方法调用类变量
        # 局部变量
        a = 0
        print(a)
        print("我闪-------")

    # 类方法
    @classmethod
    def heal(cls):
        print("治疗————")
        print(cls.game)  # 使用cls来调用类变量
        print("治疗————")

    # 静态方法
    @staticmethod
    def ignit():
        print("点燃>>>>>>>")
        print(Hero.heal())
        print("点燃>>>>>>>")


yasuo = Hero("Yasuo")
print(yasuo.game)
yasuo.game = "DNN"
print(yasuo.game)
print(Hero.game)
print(yasuo.name)

# 实例方法调用
yasuo.flash()

# 类方法调用
Hero.heal()
yasuo.heal()

# 静态方法调用
yasuo.ignit()
# Hero.ignit()
