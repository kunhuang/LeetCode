class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l1 = [('', 0)]
        l2 = []
        for i in range(2*n):
            for s in l1:
                if s[1] == 0:
                    l2.append([s[0]+'(', 1])
                elif s[1] == 2*n-i:
                    l2.append([s[0]+')', s[1]-1])
                else:
                    l2.append([s[0]+'(', s[1]+1])
                    l2.append([s[0]+')', s[1]-1])
            l1 = l2[:]
            l2 = []
        return [s[0] for s in l1]

print Solution().generateParenthesis(100)