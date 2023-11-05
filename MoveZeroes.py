class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):
            p = nums[i]
            if p != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
