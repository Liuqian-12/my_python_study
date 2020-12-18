class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，可以访问对象的私有属性
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")
# 私有属性不能被外部直接访问
# print(xiaofang.__age)
# xiaofang.secret()
# 私有方法也不能被外部直接访问
# xiaofang.__secret()
        
        