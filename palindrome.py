class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        reversed_num = int(str(x)[::-1])
        if reversed_num==x:
            return True
        else:
            return False
