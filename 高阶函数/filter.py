# filter()这个高阶函数，关键在于正确实现一个“筛选”函数
L1 = list(filter(lambda x: x % 2 == 1, range(1, 6)))
print(L1)

a=[1,2,3,4,5,6,7,8]
b = filter(lambda x: x>5,a)
print(list(b))