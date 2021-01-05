from python单例模式.singleton import singleton as s1
from python单例模式.singleton import singleton as s2

print(s1, id(s1))
print(s2, id(s2))

"""
多次导入该实例，其实调用的是一个地址
"""