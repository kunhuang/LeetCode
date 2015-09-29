class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x, positive = (x, 1) if x > 0 else (-x, -1)
        result = 0
        while(x > 0):
            result = result*10 + x%10
            x = x/10
        return positive*result if result < 0x7fffffff else 0

print Solution().reverse(1534236469)
