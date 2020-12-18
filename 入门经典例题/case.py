class Solution:
    def twoSum(self,nums,target):
        hashmap = {}
        for idx, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num],idx]
            else:
                hashmap[num] = idx

a=Solution()
nums=[2,7,11,15]
target=9
print(a.twoSum(nums,target))