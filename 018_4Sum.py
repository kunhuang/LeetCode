class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        hash_ = {}
        for num in nums:
            hash_[num] = hash_.get(num, 0) + 1

        for num in hash_.keys():
            if hash_[num] >= 2:
                if 4*num < target and hash_.get(float(target)/2-num, 0) >= 2:
                    result.append([num, num, target/2-num, target/2-num])
                for num_ in hash_.keys():
                    if num_ == num:
                        continue
                    if hash_.get(target-2*num-num_, 0) > 0 and num_ < target-2*num-num_ and target-2*num-num_ != num:
                        result.append(sorted([num, num, num_, target-2*num-num_]))
            if hash_[num] >= 3:
                if 4*num != target  and hash_.get(target-3*num, 0) > 0:
                    if num > target-3*num:
                        result.append([target-3*num, num, num, num])
                    else:
                        result.append([num, num, num, target-3*num])    
            if hash_[num] >= 4:
                if 4*num == target:
                    result.append([num]*4)

        nums = hash_.keys()
        if len(nums) < 4:
            return result
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                s, t = j+1, len(nums)-1
                while s != t:
                    if nums[i]+nums[j]+nums[s]+nums[t] < target:
                        s += 1
                    elif nums[i]+nums[j]+nums[s]+nums[t] > target:
                        t -= 1
                    else:
                        result.append([nums[i], nums[j], nums[s], nums[t]])
                        s += 1
        return result

print Solution().fourSum([1,0,-1,0,-2,2], 0)