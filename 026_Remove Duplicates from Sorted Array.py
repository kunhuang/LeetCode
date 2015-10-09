class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        current_num = nums[0]
        unique_pos = 0
        for i in range(len(nums)):
            if nums[i] == current_num:
                continue
            unique_pos += 1
            nums[unique_pos] = current_num = nums[i]

        return unique_pos+1

nums = [1, 1, 2,2,3]
print Solution().removeDuplicates(nums)
print nums