class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        O(m+n)
        """
        while i <= m + n -1 and j <= n - 1:
            if nums2[0] <= nums2[j]:
                nums1[i], nums2[0] = nums2[0], nums1[i]
                i += 1
            else:

        while i - j <= m-1 and j <= n-1:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                for k in range(m + j, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                j += 1
                i += 1

        if j <= n - 1:
            for k in range(i, m + n):
                nums1[k] = nums2[j+k-i]
    def merge_solution1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        O(m*n)
        """
        i = j = 0
        while i - j <= m-1 and j <= n-1:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                for k in range(m + j, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                j += 1
                i += 1

        if j <= n - 1:
            for k in range(i, m + n):
                nums1[k] = nums2[j+k-i]

Solution().merge(nums1, 3, nums2, 2)

print nums1