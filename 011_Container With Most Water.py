class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = (0, len(height)-1)
        maxwater = j*min(height[0], height[-1])
        while i != j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            maxwater = max(maxwater, (j-i)*min(height[i], height[j]))
        return maxwater

print Solution().maxArea([3])