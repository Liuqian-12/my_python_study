class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

a = Solution()
nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
print(a.pivotIndex(nums))


