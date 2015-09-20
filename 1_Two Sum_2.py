class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target/2. in nums and nums.count(target/2.) == 2:
            return [i+1 for i, x in enumerate(nums) if x == target/2]
        map_ = {}
        for k, v in enumerate(nums):
            map_[v] = k
        for index1, v in enumerate(nums):
            if map_.get(target-v, None) and v*2 != target:
                return index1+1, map_[target-v]+1

nums = [0,4,3,0]
target = 0
print Solution().twoSum(nums, target)