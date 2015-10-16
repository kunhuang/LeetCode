import pdb
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        for i in range(len(candidates)):
            if candidates[i] >= target:
                break
        candidates = candidates[:i+1]
    
        hash_ = {}
        for num in candidates:
            hash_[num] = hash_.get(num, 0) + 1
        stack = [[]]
        new_stack = []
        result = []
        for num in sorted(hash_):
            # pdb.set_trace()
            for combination in stack:
                new_stack.append(combination[:])
                for i in range(1, hash_[num]+1):
                    if sum(combination) + i*num == target:
                        result.append(combination[:]+[num]*i)
                        break
                    elif sum(combination) + i*num < target:
                        new_stack.append(combination[:]+[num]*i)
            stack = new_stack[:]
            new_stack = []

        return result

print Solution().combinationSum2([10,1,2,7,6,1,5], 8)