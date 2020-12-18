class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")

        # self.name = "tom"
        
        # self.属性 = 形参
        self.name = new_name

    def eat(self):
        print("%s 吃鱼" % self.name)

    
# 使用类名（）创建对象的时候，会自动调用初始化方法 _init_
Tom = Cat("Tom")

print(Tom.name)
Tom.eat()

lazy_cat = Cat("lazytom")
lazy_cat.eat()
