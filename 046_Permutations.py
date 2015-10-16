import pdb
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hash_ = {}
        for num in nums:
            hash_[num] = hash_.get(num, 0) + 1

        result = [[]]
        tmp_result = []

        while True:
            for permutation in result:
                if len(permutation) < len(nums):
                    for num in hash_.keys():
                        if len(permutation) + hash_[num] - permutation.count(num) == len(nums):
                            tmp_result.append(permutation+[num]*(hash_[num] - permutation.count(num)))
                        elif len(permutation) == 0 or permutation[-1] != num:
                            for j in range(hash_[num] - permutation.count(num)):
                                tmp_result.append(permutation+[num]*(j+1))
                elif len(permutation) == len(nums):
                    tmp_result.append(permutation)
            result = tmp_result[:]
            tmp_result = []
            if min([len(permutation) for permutation in result]) == len(nums):
                break

        return result

print Solution().permute([1,2,3])