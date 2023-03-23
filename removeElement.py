class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        current = 0
        for i in range (0, len(nums)):
            if nums[i] != val:
                temp = nums[current]
                nums[current] = nums[i]
                nums[i] = temp
                current += 1
        return current
