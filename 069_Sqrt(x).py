import pdb
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return 0
        if x == 0:
            return 0
        if x == 1 or x == 2 or x == 3:
            return 1

        i = 2

        while(True):
            if (i+1)*(i+1) <= x:
                i = (x/i+i)/2
            elif i*i > x:
                i = (x/i+i)/2
            elif i*i <= x < (i+1)*(i+1):
                return i
            

for i in range(1000):
    # pdb.set_trace()
    print Solution().mySqrt(i)