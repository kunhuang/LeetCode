class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tail = 0
        for num in nums:
            if num != 0:
                nums[tail] = num
                tail += 1
        for i in range(tail, len(nums)):
            nums[i] = 0

nums = [0,0,1]
Solution().moveZeroes(nums)
print nums
