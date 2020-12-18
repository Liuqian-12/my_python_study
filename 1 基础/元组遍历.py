# 第一种：for in
tuple1 = ("a", "1", 1, "b", "c", "c")
for value in tuple1:
    print("value=", value)
print("--------------------")

# 第二种：使用内置函数enumerate()
tuple2 = ("a", "1", 1, "b", "c", "c")
for index, value in enumerate(tuple2):
    print("index=", index, "value=", value)
print("-------------------- ")

# 第三种：使用range遍历
tuple3 = ("a", "1", 1, "b", "c", "c")
for index in range(len(tuple3)):
    print("index=", index, "value=", tuple3[index])
print("--------------------")

# 第四种：iter遍历
tuple4 = ("a", "1", 1, "b", "c", "c")
for value in iter(tuple4):
    print("value=", value)


"""
四种方式遍历元组的语法：

for item in tuple:
    pass

for index in range(len(tuple)):
    pass

for index, value in enumerate(tuple):
    pass

for item in iter(tuple):
    pass
"""