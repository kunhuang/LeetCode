class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if n < -1:
            n = -n
            return 1/(x*self.myPow(x, n/2)**2) if n%2 else 1/(self.myPow(x, n/2)**2)
        return x*self.myPow(x, n/2)**2 if n%2 else self.myPow(x, n/2)**2

print Solution().myPow(34.00515, -3)