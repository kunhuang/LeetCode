class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, 0, target)
    def binary_search(self, nums, head_index, target):
        if len(nums) == 0:
            return head_index
        if len(nums) == 1:
            return head_index if nums[0] >= target else head_index+1
        pivot = len(nums)/2
        if nums[pivot] == target:
            return head_index + pivot
        elif nums[pivot] > target:
            return self.binary_search(nums[:pivot], head_index, target)
        else:
            return self.binary_search(nums[pivot+1:], head_index+pivot+1, target)

print Solution().searchInsert([1,1,1,3,5], 0)