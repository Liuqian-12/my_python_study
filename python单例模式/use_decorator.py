"""
使用装饰器实现单例模式
"""
def Singleton(cls):
    _instance = {}  # 创建空字典

    def get_singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return get_singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

if __name__ == '__main__':
    a1 = A(2)
    a2 = A(3)
    a3 = A()
    print(a1, a2, a3)
    print(a1 is a2)
    print(a1.x, a2.x)
    print(a1.a, a2.a)
    
