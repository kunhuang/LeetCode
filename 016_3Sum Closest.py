import pdb
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_dif = abs(sum(nums[:3])-target)
        closest_sum = sum(nums[:3])
        for i in range(1, len(nums)-1):
            j, k = (0, len(nums)-1)
            while j != k:
                if j == i:
                    j += 1
                    continue
                elif k == i:
                    k -= 1
                    continue
                sum_ = nums[i]+nums[j]+nums[k]
                if abs(sum_-target) < closest_dif:
                    closest_sum = sum_
                    closest_dif = abs(sum_-target)
                if sum_ < target:
                    j += 1
                elif sum_ > target:
                    k -= 1
                else:
                    return closest_sum
        return closest_sum

print Solution().threeSumClosest([-1, 2, 2, 1, 1, -4], 1)
