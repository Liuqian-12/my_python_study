"""
字典与列表的最大区别就是：
字典中强调的是‘键值对’，key与value一一对应
"""


# 字典的创建
a1 = {"name": "xiaoming", "sex": "man", "id": 1}
print(a1)

a2 = dict(id=1, name="xiaoming")
print(a2)

a3 = {}
a3["name"] = "xiaoming"
a3["id"] = 1
print(a3)

# 字典推导式
a4 = {x: x**2 for x in [1, 2, 3]}
print(a4)


# key是字典的键，返回的是对应的值value
# get方法获取键的值，若键不存在，则返回设定的默认值default（默认为None）
print(a1["name"])
print(a1.get("name"))
print(a1.get(1))


# 遍历
for i in a1.keys():
    print(i, a1[i])

for i in a1:
    print(i, a1[i])

for keys, values in a1.items():
    print(keys, values)


# 排序
# 1.借助.keys()方法和list()函数将键提取成list，对list排序后输出
D = {'a': 1, 'c': 3, 'b': 2}
D1 = list(D.keys())
print(D1)
D1.sort()
for i in D1:
    print(i, D[i])

# 2.借助内置的sorted()函数可对任意对象类型排序，返回排序后的结果
D2 = {'a': 1, 'c': 3, 'b': 2}
print(sorted(D2))
for i in sorted(D2):
    print(i, D[i])

