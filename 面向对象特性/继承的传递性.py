class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def drak(self):
        print("叫")

class Xiaotq(Dog):
    def fly(self):
        print("飞")

xiaotq = Xiaotq()

xiaotq.fly()
xiaotq.drak()
xiaotq.eat()

