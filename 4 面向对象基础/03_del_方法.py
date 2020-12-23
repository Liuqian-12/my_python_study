class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

# tom是个全局变量
Tom = Cat("Tom")
print(Tom.name)

# del Tom
print("-" * 50)


# 生命周期