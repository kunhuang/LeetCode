class Solution(object):
    def isMatch(self, string, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # Initialization
        n = len(pattern)
        m = len(string)
        if n == 0 and m == 0:
            return True

        match = []
        for i in range(n+1):
            match.append([False]*(m+1))

        match[0][0] = True
        for i in range(1, n+1):
            if pattern[i-1] == '*':
                match[i][0] = match[i-2][0]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if pattern[i-1] == '*':
                    match[i][j] = match[i-2][j] or ((match[i][j-1] or match[i-2][j-1]) and (string[j-1] == pattern[i-2] or pattern[i-2] == '.'))
                else:
                    match[i][j] = match[i-1][j-1] and (string[j-1] == pattern[i-1] or pattern[i-1] == '.')
                # print pattern[:i], string[:j], match[i][j]

        return match[n][m]

string = "aab"
pattern = "c*a*b"

print Solution().isMatch(string, pattern)