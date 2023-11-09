class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
		    return False
	
	return str(x) == str(x)[::-1]
    '''    if x<0:
		    return False
        inputNum = x
	newNum = 0
	while x>0:
		newNum = newNum * 10 + x%10
		x = x//10
	return newNum == inputNum '''
