class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        for i in range(len(string)/2):
            if string[i] != string[len(string)-1-i]:
                return False
        return True