class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ')
        str_list = s.split(' ')
        return len(str_list[-1])

print Solution().lengthOfLastWord("Hello World ")