# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
        
# g = foo()
# print(next(g))
# print("*"*20)
# print(g.send(7))
# print(next(g))

def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
        
for n in foo(0):
    print(n)