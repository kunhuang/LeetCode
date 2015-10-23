class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = nums[0]

        for num in nums:
            if max_sum < num:
                max_sum = num
        if max_sum < 0:
            return max_sum

        current_sum = 0

        for num in nums:
            if num == 0:
                continue
            if num < 0:
                if current_sum > max_sum:
                    max_sum = current_sum
                if current_sum + num <= 0:
                    current_sum = 0
                else:
                    current_sum += num
            if num > 0:
                current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        return max_sum

print Solution().maxSubArray([-2, -5])