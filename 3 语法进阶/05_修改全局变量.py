num = 10

def demo1():

    # global 修改全局变量
    global num
    num = 99
    print("demo1 --> %d" % num)

def demo2():
    print("demo2 --> %d" % num)

demo1()
demo2()