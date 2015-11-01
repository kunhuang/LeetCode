class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        end = len(nums) - 1
        start = 0
        i = 0
        while i <= end:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                i += 1
                start += 1
            else:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1


    def sortColors_(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        index = 0
        for i in range(3):
            for j in range(count[i]):
                nums[index] = i
                index += 1

nums = [1,0]
Solution().sortColors(nums)
print nums