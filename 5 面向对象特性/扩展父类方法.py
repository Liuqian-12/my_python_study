class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def drak(self):
        print("叫")

class Xiaotq(Dog):
    def fly(self):
        print("飞")

    # def drak(self):
    #     print("神狗叫")

    def drak(self):
        
        # 1.针对子类特有的需求，编写代码
        print("神狗叫")

        # 2.使用super()调用父类的方法
        #  super().drak()
    
        #  父类名.方法(self)
        #  Dog.drak(self)

        #  注意：如果使用子类调用方法，会出现递归调用 - 死循环！！！
        #  Xiaotq.drak(self)
        

        # 3.其他子类代码 
        print("&(*^*^&%$")

xtq = Xiaotq()

# 重写之后，在运行时，只会调用子类中重写的方法，而不再会调用父类封装的方法
xtq.drak()