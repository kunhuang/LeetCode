class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {' ':0, 'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        s = s+' '
        for i in range(len(s)-1):
            if symbols[s[i]] < symbols[s[i+1]]:
                result -= symbols[s[i]]
            else:
                result += symbols[s[i]]
        return result

print Solution().romanToInt("MCCCXI")