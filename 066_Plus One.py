class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        c = 1
        result = [0]*len(digits)
        for i in range(len(digits)-1, -1, -1):
            result[i] = digits[i] + c
            if result[i] == 10:
                result[i] = 0
            else:
                c = 0
        if c == 1:
            result.insert(0, 1)
        return result

print Solution().plusOne([8,1,1])