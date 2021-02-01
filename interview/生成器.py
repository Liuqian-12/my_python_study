def fib(max):
    """斐波那契数列"""
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
# 普通函数调用直接返回结果
# print(fib(6))

def fib_generator(max):
    """生成器"""
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# generator函数的“调用”实际返回一个generator对象
# print(fib_generator(6))
# 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
# for n in fib_generator(6):
#     print(n)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
# g = fib_generator(6)
# while True:
#     try:
#         x = next(g)
#         print('g: ', x)
#     except StopIteration as e:
#         print('Generator return value: ', e.value)
#         break

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))