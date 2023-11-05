class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evens = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                evens += 1
        return evens
