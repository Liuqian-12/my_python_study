class A:
    def test(self):
        print("A--test")

    def demo(self):
        print("A--demo")


class B:
    def test(self):
        print("B--test")
    def demo(self):
        print("B--demo")


class C(B, A):
    """"""
    pass


c = C()
c.test()
c.demo()
