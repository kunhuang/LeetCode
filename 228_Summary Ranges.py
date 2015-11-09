class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """  
        start = 0
        result = [] 
        if len(nums) == 0:
            return []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                continue
            else:
                if start != i - 1:
                    result.append(str(nums[start])+"->"+str(nums[i-1]))
                else:
                    result.append(str(nums[start]))
                start = i
        if start != len(nums)-1:
            result.append(str(nums[start])+"->"+str(nums[-1]))
        else:
            result.append(str(nums[start]))
        return result

print Solution().summaryRanges([])