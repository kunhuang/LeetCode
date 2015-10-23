import pdb
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        head_index = self.find_start(nums, 0, target)
        end_index = self.find_end(nums, 0, target)
        return [head_index, end_index]

    def find_start(self, nums, head_index, target):
        # pdb.set_trace()
        if nums is None or len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return head_index
            else:
                return -1    

        pivot = len(nums)/2
        if nums[pivot] < target:
            if len(nums)-1>pivot and nums[pivot+1] == target:
                return head_index + pivot + 1
            else:
                return self.find_start(nums[pivot+1:], head_index+pivot+1, target)
        elif nums[pivot] > target:
            return self.find_start(nums[:pivot], head_index, target)
        else:
            if nums[pivot-1] != target:
                return head_index + pivot
            else:
                return self.find_start(nums[:pivot], head_index, target)

    def find_end(self, nums, head_index, target):
        # pdb.set_trace()
        if nums is None or len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return head_index
            else:
                return -1    

        pivot = len(nums)/2
        if nums[pivot] > target:
            if nums[pivot-1] == target:
                return head_index + pivot - 1
            else:
                return self.find_end(nums[:pivot], head_index, target)
        elif nums[pivot] < target:
            return self.find_end(nums[pivot+1:], head_index+pivot+1, target)
        else:
            if len(nums)-1 == pivot or nums[pivot+1] != target:
                return head_index + pivot
            else:
                return self.find_end(nums[pivot+1:], head_index+pivot+1, target)

print Solution().searchRange([1,2,6], 6)