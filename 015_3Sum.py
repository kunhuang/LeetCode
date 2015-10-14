import pdb
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        hash_ = dict()
        double_elements = []
        for i in nums:
            hash_[i] = hash_.get(i, 0) + 1
            if hash_[i] == 2:
                double_elements.append(i)
            
        for element in double_elements:
            if element == 0:
                if hash_[element] >= 3:
                    result.append([0, 0, 0])
            elif hash_.get(-2*element) > 0:
                if element > 0:
                    result.append([-2*element, element, element])
                else:
                    result.append([element, element, -2*element])
        nums = hash_.keys()
        if len(nums) < 3:
            return result

        nums.sort()
        for i in range(len(nums)-2):
            s, t = i + 1, len(nums)-1
            while s != t:
                if nums[i] + nums[s] + nums[t] < 0:
                    s += 1
                elif nums[i] + nums[s] + nums[t] > 0:
                    t -= 1
                else:
                    result.append([nums[i], nums[s], nums[t]])
                    s += 1

        return result

print Solution().threeSum([0, 0])

