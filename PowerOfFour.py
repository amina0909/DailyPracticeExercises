class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        return n>0 and log(n,4).is_integer() 
