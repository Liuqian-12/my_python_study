print("-------------------对象所属的类之间没有继承关系------------------------")

# 调用同一个函数fly(), 传入不同的参数（对象），可以达成不同的功能
class Duck(object):                                  # 鸭子类
    def fly(self):
        print("鸭子沿着地面飞起来了")

class Swan(object):                                  # 天鹅类
    def fly(self):
        print("天鹅在空中翱翔")

class Plane(object):                                 # 飞机类
    def fly(self):
        print("飞机隆隆地起飞了")

def fly(obj):                                        # 实现飞的功能函数
    obj.fly()

duck = Duck()
fly(duck)

swan = Swan()
fly(swan)

plane = Plane()
fly(plane)


print("-------------------对象所属的类之间有继承关系(应用更广)------------------------")

class gradapa(object):
    def __init__(self,money):
        self.money = money
    def p(self):
        print("this is gradapa")
 
class father(gradapa):
    def __init__(self,money,job):
        super().__init__(money)
        self.job = job
    def p(self):
        print("this is father,我重写了父类的方法")
 
class mother(gradapa): 
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job
 
    def p(self):
         print("this is mother,我重写了父类的方法")
         
#定义一个函数，函数调用类中的p()方法
def fc(obj): 
    obj.p()

gradapa1 = gradapa(3000) 
father1 = father(2000,"工人")
mother1 = mother(1000,"老师")

#这里的多态性体现是向同一个函数，传递不同参数后，可以实现不同功能.
fc(gradapa1)            
fc(father1)
fc(mother1)


print('------------------------------')
class Animal(object):   #编写Animal类
    def run(self):
        print("Animal is running...")

class Dog(Animal):  #Dog类继承Amimal类，没有run方法
    pass

class Cat(Animal):  #Cat类继承Animal类，有自己的run方法
    def run(self):
        print('Cat is running...')
    pass

class Car(object):  #Car类不继承，有自己的run方法
    def run(self):
        print('Car is running...')

class Stone(object):  #Stone类不继承，也没有run方法
    pass

def run_twice(animal):
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Car())
run_twice(Stone())