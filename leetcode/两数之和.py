class Solution:
    def Sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break
                else:
                    continue

s1 = Solution()
list1 = [1, 2, 3, 4]
target1 = 4
sum = s1.Sum(list1, target1)
print(sum)




        


    