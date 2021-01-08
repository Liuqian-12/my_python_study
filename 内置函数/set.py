"""
set是集合
里面不能包含重复的元素
接收一个list作为参数
"""
list1 = [-1, 1, 2, 4, 3, 0, "xiaoming"]
s = set(list1)
print(s)

# 使用add(key)往集合中添加元素，重复的自动过滤
s.add(4)
s.add(5)
print(s)

# 通过remove(key)方法可以删除元素
s.remove("xiaoming")
s.remove(-1)
print(s)

# set还可以像数学上那样求交集和并集
list2 = ["a", "b", "c", "d", 1, 2]
s2 = set(list2)
s3 = s & s2
s4 = s | s2
print(s3)
print(s4)

# 逐个遍历
for i in s:
    print(i)