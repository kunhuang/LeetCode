from random import shuffle
import pdb
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums, indexs = self.quicksort_with_index(nums)
        i, j = (0, len(nums)-1)
        sum_ = sorted_nums[i] + sorted_nums[j]
        while(i<j and sum_!=target):
            if sum_>target:
                j-=1
            else:
                i+=1
            sum_ = sorted_nums[i] + sorted_nums[j]
        return [indexs[i]+1, indexs[j]+1] if indexs[i] < indexs[j] else [indexs[j]+1, indexs[i]+1]
    def quicksort_with_index(self, l):
        def quicksort_(l):
            if len(l)<=10:
                for i in range(len(l)):
                    for j in range(i, len(l)):
                        if l[i][0] > l[j][0]:
                            l[i], l[j] = l[j], l[i]
                return l
            else:
                shuffle(l)
                return quicksort_([n for n in l[1:] if n[0] <= l[0][0]]) + [l[0]] + quicksort_([n for n in l[1:] if n[0] > l[0][0]])
        return zip(*quicksort_(zip(l, range(len(l)))))
s = Solution()
nums = [4,2,1,3]
target = 7
print s.twoSum(nums, target) 