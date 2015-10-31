class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = [[]]
        for num in nums:
            current = result[:]
            # Tricky point, have to use the copy of result, otherwise it's a infinite loop
            for subset in current:
                new_subset = subset[:]
                new_subset.append(num)
                result.append(new_subset)

        map(lambda x: x.sort(), result)
        return result

print Solution().subsets([1,2,3])