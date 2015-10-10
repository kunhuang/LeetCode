import pdb
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            pdb.set_trace()
            if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
                return i
        return -1

print Solution().strStr("a", "a")