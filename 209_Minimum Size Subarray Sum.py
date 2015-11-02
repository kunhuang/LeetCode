class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        start = 0
        end = 0
        current_sum = nums[0]
        min_length = len(nums)+1

        while end <= len(nums)-1:
            if current_sum < s:
                end += 1
                if end <= len(nums)-1:
                    current_sum += nums[end]
            elif current_sum >= s:
                if end - start + 1 < min_length:
                    min_start = start
                    min_end = end
                    min_length = end - start + 1
                current_sum -= nums[start]
                start += 1

        return min_length if min_length <= len(nums) else 0

print Solution().minSubArrayLen(4, [4,1,1,1,1,2])