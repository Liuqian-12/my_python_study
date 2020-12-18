# 给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

# 我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

class Solution:
    def pivotIndex(self, nums):
        S = sum(nums)
        leftnum = 0
        for i, item in enumerate(nums):
            if leftnum == S-leftnum-item:
                return i
            leftnum += item
        return -1

a = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(a.pivotIndex(nums))

