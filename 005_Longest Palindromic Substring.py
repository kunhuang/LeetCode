class Solution(object):
    def longestPalindrome(self, s):
        """
        O(N^2) Solution
        :type s: str
        :rtype: str
        """
        max_length = 0
        max_string = ""
        for i in range(len(s)):
            for j, k in [(i-1, i+1), (i, i+1)]:
                while(j>=0 and k<=len(s)-1 and s[j]==s[k]):
                    j -= 1
                    k += 1
                if k-j-1 > max_length:
                    max_length = k-j-1
                    max_string = s[j+1:k]
        return max_string


s = "ccccccabaaabaac"
print Solution().longestPalindrome(s)
