import pdb
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums2)+len(nums1))%2:
            if len(nums1)>len(nums2):
                return self.findNthSortedArrays(nums1, nums2, (len(nums2)+len(nums1))/2+1)
            return self.findNthSortedArrays(nums2, nums1, (len(nums2)+len(nums1))/2+1)
        else:
            if len(nums1)>len(nums2):
                return (self.findNthSortedArrays(nums1, nums2, (len(nums2)+len(nums1))/2)+self.findNthSortedArrays(nums1, nums2, (len(nums2)+len(nums1))/2+1))/2.
            return (self.findNthSortedArrays(nums2, nums1, (len(nums2)+len(nums1))/2)+self.findNthSortedArrays(nums2, nums1, (len(nums2)+len(nums1))/2+1))/2.

    def findNthSortedArrays(self, nums1, nums2, n):
        if len(nums2) == 0:
            return nums1[n-1]
        if n == 1:
            return nums1[0] if nums1[0] < nums2[0] else nums2[0]

        length2 = len(nums2) if n/2 > len(nums2) else n/2
        length1 = n - length2
        
        if nums1[length1-1] < nums2[length2-1]:
            nums1 = nums1[length1:]
            nums2 = nums2[:length2]
            if len(nums1)>len(nums2):
                return self.findNthSortedArrays(nums1, nums2, n-length1)
            return self.findNthSortedArrays(nums2, nums1, n-length1)
        elif nums1[length1-1] > nums2[length2-1]:
            nums1 = nums1[:length1]
            nums2 = nums2[length2:]
            if len(nums1)>len(nums2):
                return self.findNthSortedArrays(nums1, nums2, n-length2)
            return self.findNthSortedArrays(nums2, nums1, n-length2)
        else:
            return nums1[length1-1]

print Solution().findMedianSortedArrays([1], [1])