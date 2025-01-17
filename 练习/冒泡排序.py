def bubble_sort(alist):
    n = len(alist)
    if n<=1:
        return alist
    for i in range(n):
        for j in range(0, n-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist


alist = [4, 3, 6, 7, 8, 2, 1]
bubble_sort(alist)

"""
冒泡排序
比较相邻的元素。如果第一个比第二个大，就交换它们两个；
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
针对所有的元素重复以上的步骤，除了最后一个；
重复步骤1~3，直到排序完成。

冒泡排序对n个数据操作n-1轮，每轮找出一个最大（小）值。
操作只对相邻两个数比较与交换，每轮会将一个最值交换到数据列首（尾），像冒泡一样。
每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。
额外空间开销出在交换数据时那一个过渡空间，空间复杂度O(1)
"""