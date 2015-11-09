class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        if len(citations) == 0:
            return 0
        for i in range(1, len(citations)+1):
            if citations[len(citations)-i] > i:
                continue
            elif citations[len(citations)-i] == i:
                return i
            else:
                return i - 1
        return i

citations = [0,0,0,0]
print Solution().hIndex(citations)