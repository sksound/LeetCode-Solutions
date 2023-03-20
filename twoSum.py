class Solution(object):
    def twoSum(self, nums, target):
        copyList = nums
        for i in range (0, len(nums)):
            for x in range (0, len(copyList)):
                if nums[i] + copyList[x] == target and i != x:
                    return i, x
