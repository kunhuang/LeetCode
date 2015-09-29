class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = ""
        lens = map(len, strs)
        for i in range(min(lens)):
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    return prefix
            prefix = prefix+strs[0][i]
        return prefix

print Solution().longestCommonPrefix([])