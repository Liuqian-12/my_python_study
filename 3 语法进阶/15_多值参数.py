def demo(num, *arg, **karg):
    print(num)
    print(arg)
    print(karg)

demo(1, 2, 3, 4, name = "xiaoming", age = 18)
