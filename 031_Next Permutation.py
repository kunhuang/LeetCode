import pdb
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        if len(nums) == 1:
            return

        swap_start = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                swap_start = i-1
                break
        if swap_start == -1:
            self.reverse(0, len(nums)-1, nums)
            return 

        exchange = len(nums)-1
        for i in range(swap_start+2, len(nums)):
            if nums[swap_start] >= nums[i]:
                exchange = i-1
                break
        if exchange == len(nums):
            tmp = nums[exchange]
            nums[exchange] = nums[swap_start+1]
            nums[swap_start+1] = nums[swap_start]
            nums[swap_start] = tmp

            if exchange - swap_start > 3:
                self.reverse(swap_start+2, exchange-1, nums)
        else:
            nums[exchange], nums[swap_start] = nums[swap_start], nums[exchange]
            self.reverse(swap_start+1, len(nums)-1, nums)

    def reverse(self, start, end, l):
        for i in range((end-start+1)/2):
            l[start+i], l[end-i] = l[end-i], l[start+i]

nums = [1,3,2]
Solution().nextPermutation(nums)
print nums