class A:
    # pass
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的共有方法")

class B(A):
    def demo(self):
        print("子类方法 %d" % self.num1)
        self.test()
        # 在子类的对象方法中，不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)

        # 不能调用父类的私有方法
        # self.__test()
   
    


# 创建一个子类对象
b = B()
print(b)

# 在外界不能直接访问对象的私有属性/调用私有方法

# 在外界访问对象的公有属性/调用公有方法
b.demo()
