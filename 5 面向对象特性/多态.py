class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳" % self.name)

class xiaotq(Dog):
    def game(self):
        print("%s 飞到天上玩耍..." % self.name)

class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 一起玩" % (self.name, dog.name))

        dog.game()


# 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = xiaotq("旺财")
xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)
    