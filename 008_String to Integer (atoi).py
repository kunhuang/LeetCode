import pdb
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if len(str) == 0:
            return 0
        positive = (str[0] != '-')
        if str[0] == '-' or str[0] == '+':
            str = str[1:]
        result = 0
        for i in range(len(str)):
            digit = ord(str[i])-ord('0')
            if digit > 9 or digit < 0:
                break
            else:
                result = result*10 + digit
        result = result if positive else -result
        return (0x7fffffff if result > 0x7fffffff else 
                -0x80000000 if result < -0x80000000 else 
                result)
print Solution().myAtoi("1")