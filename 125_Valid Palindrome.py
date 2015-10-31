class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = []
        for c in s:
            if 'A'<= c <='Z':
                new_s.append(chr(ord(c)-ord('A')+ord('a')))
            elif 'a'<= c <='z' or '0' <= c <= '9':
                new_s.append(c)
            
        for i in range(len(new_s)/2):
            if new_s[i] != new_s[len(new_s) - 1 - i]:
                return False

        return True

print Solution().isPalindrome("1a2")