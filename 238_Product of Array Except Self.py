class Solution(object):
    def productExceptSelf_solution2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time: O(N)
        Space: O(1), not including the output space
        """
        # TODO
        pass
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time: O(N)
        Space: O(N)
        """
        if nums is None or len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [1]

        sub_product_forward = nums[:]
        sub_product_backward = nums[:]

        for i in range(1, len(sub_product_forward)):
            sub_product_forward[i] *= sub_product_forward[i-1]
    
        for i in range(len(sub_product_backward)-2, -1, -1):
            sub_product_backward[i] *= sub_product_backward[i+1]        

        result = [1]*len(nums)
        result[0] = sub_product_backward[1]
        result[-1] = sub_product_forward[-2]
        for i in range(1, len(result)-1):
            result[i] = sub_product_forward[i-1]*sub_product_backward[i+1]
        
        return result
    
    def productExceptSelf_solution1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time: O(N^2)
        Space: o(N)
        """
        if nums is None or len(nums) == 0:
            return nums

        current_product = [1, 1]
        
        for i, num in enumerate(nums[1:]):
            for j in range(len(current_product[:-1])):
                current_product[j] *= num
            current_product.append(current_product[-1]*num)

        return current_product[:-1]

print Solution().productExceptSelf([1,2,3,4])
