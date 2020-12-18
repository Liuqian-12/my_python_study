from functools import wraps
def foo():
    print("hello foo")
 
print(foo.__name__)
#####################
 
def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
 
        print (func.__name__ + " was called")
        return func(*args, **kwargs)
 
    return wrapper
 
 
@logged
def cal(x):
   return x + x * x
 
 
print(cal.__name__)