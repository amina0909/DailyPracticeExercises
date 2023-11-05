class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares_list = []
        for num in nums:
            val = num*num
            squares_list.append(val)
        return sorted(squares_list)
