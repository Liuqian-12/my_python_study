# 1+11+111+1111+11111的和
# def fun(n):
#     sum = 0
#     x = 0
#     for i in range(1, n):
#         x = x*10 +1
#         sum += x
#     print(sum)

# fun(6)

# s=0
# t=0
# for i in range(5):
#    t=t*10+1
#    s+=t
# print(s)


# 冒泡排序
# def bubble_sort(alist):
#     n = len(alist)
#     for i in range(n):
#         count = 0
#         for j in range(0, n-1):
#             if alist[j] > alist[j+1]:
#                 alist[j], alist[j+1] = alist[j+1], alist[j]
#                 count += 1

#     print(alist)


# alist = [5, 3, 4, 7]
# bubble_sort(alist)


# 打印9*9乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (i, j, i*j), end=' ')
#     print()
            
# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i!=j and i!=k and j!=k:
#                 print(i,j,k)


# for i in range(3):
#     str = ''
#     for j in range(5-i):
#         if i == j or i + j == 4 :
#             str += 'v'
#         else :
#             str += ' '
#     print(str)

res1 = {'code': 1, 'msg': '登陆成功'}
res2 = {'code': 0, 'msg': '登陆失败'}

# 用try--except捕获断言异常
try:
    assert res1 == res2
except AssertionError as e:
    print("编号A1用例不通过！")
    raise e  # 处理异常后，抛出异常
else:
    print("编号A1用例通过！")

