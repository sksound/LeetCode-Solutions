class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        r = x[::-1]
        if x == r:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
