"""
列表的索引
"""
list1 = [1, 2, 3, 4, 5, 0]
print(list1[1])
# 当下标为负数时则代表从后往前所以（或理解为长度+负下标），即-1代表最后一个元素，-2代表倒数第2个元素
print(list1[-1])
for i in list1:
    print(i)
print("-------------------")


"""
列表的切片操作
"""


"""
列表删除元素
"""
del(list1[0])
print(list1)

a = list1.pop(2)
print(list1)

list1.remove(5)
print(list1)

list1.clear()
print(list1)
print("-------------------")


"""
列表的拼接
"""
list2 = [1, 2]
list3 = [3]
print(list2+list3)
list2.extend(list3) # 在list1后面接上list2
print(list2)
print("-------------------")


"""
元素成员判断（判断一个元素是否存在一个列表中）
"""
a = [1, 2, 3, 4, 5]
b = 2
print(b in a)
print(b not in a)
print("-------------------")


"""
在列表中插入元素
"""
list4 = [1, 2, 4, 5]
list4.append(10) # append函数在队尾插入元素
print(list4)
list4.insert(0, 7) # list1.insert(index, data) #在指定位置（index处）插入元素data
print(list4)
print("-------------------")


"""
反转列表
"""
list5 = [1, 2, 3, 4, 5]
list5.reverse()
print(list5)
print("-------------------")

"""
计算列表中指定元素x的个数
"""
list6 = [1, 2, 4, 4, 5, 5, 5]
print(list6.count(5))
print("-------------------")


"""
查找列表中指定元素的位置
index(X) 查找list中元素X的位置（若重复出现，则以第一次出现的为准）
"""
list7 = [1, 2, 2, 3, 4, 5]
print(list7.index(2))
print("-------------------")


"""
复制一个list
"""
list8 = [1, 2, 3]
list9 = list8.copy()
print(list9)
print("-------------------")


"""
列表的排序：sort方法与sorted（）函数
"""
list10 = [(1,6),(3,4),(2,5)]
list10.sort(key=lambda x:x[1], reverse=True) # 根据第二个元素，降序排列
print(list10)

