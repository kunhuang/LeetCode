import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]

    def quick_sort(nums):
        pivot = random.randint(0, len(nums)-1)
        small = []
        large = []
        for num in [nums[:pivot], pivot[pivot:]]:
            if num < nums[pivot]:
                small.append(num)
            else:
                large.append(num)
            return [quick_sort(small), num[pivot], quick_sort(large)]

print Solution().findKthLargest([3,2,1], 1)