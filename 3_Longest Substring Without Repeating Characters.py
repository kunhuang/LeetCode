class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_s = ""
        max_ = 0
        for c in s:
            if c in current_s:
                current_s = current_s[current_s.index(c)+1:] + c
            else:
                current_s = current_s + c
                max_ = max_ if max_ > len(current_s) else len(current_s)
        return max_

print Solution().lengthOfLongestSubstring("abcabcebb")