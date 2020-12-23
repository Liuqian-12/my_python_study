class Cat:
    def eat(self):
        print("%s 吃鱼" % self.name)

    def drink(self):
        print("%s 喝水" % self.name)

tom = Cat()

tom.name = "Tom"
tom.eat()
tom.drink()

Lazy_tom = Cat()

Lazy_tom.name = "LazyTom"
Lazy_tom.eat()
Lazy_tom.drink()



