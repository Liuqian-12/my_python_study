# from functools import wraps
# def foo():
#     print("hello foo")
 
# print(foo.__name__)
# #####################
 
# def logged(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
 
#         print (func.__name__ + " was called")
#         return func(*args, **kwargs)
 
#     return wrapper
 
 
# @logged
# def cal(x):
#    return x + x * x
 
 
# print(cal.__name__)

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print("2021-1-21")


now()
print(now.__name__)