class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i <= len(nums)-1:
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

nums = []
print Solution().removeElement(nums, 1)
print nums