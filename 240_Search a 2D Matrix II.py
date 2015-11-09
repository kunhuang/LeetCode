import pdb
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        self.matrix = matrix
        self.target = target

        m, n = len(matrix), len(matrix[0])
        return self.binary_search(0, m-1, 0, n-1)
        
    def binary_search(self, top, bottom, left, right):
        if top > bottom or left > right:
            return False
        if top == bottom and left == right:
            return self.matrix[top][left]==self.target
        if self.matrix[(top+bottom)/2][(left+right)/2] > self.target:
            return (self.binary_search(top, (top+bottom)/2-1, left, (left+right)/2-1) or 
                    self.binary_search((top+bottom)/2, bottom, left, (left+right)/2-1) or 
                    self.binary_search(top, (top+bottom)/2-1, (left+right)/2, right))
        elif self.matrix[(top+bottom)/2][(left+right)/2] < self.target:
            return (self.binary_search((top+bottom)/2+1, bottom, (left+right)/2+1, right) or 
                    self.binary_search(top, (top+bottom)/2, (left+right)/2+1, right) or 
                    self.binary_search((top+bottom)/2+1, bottom, left, (left+right)/2))
        else:
            return True

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
for i in range(31):
    print i, Solution().searchMatrix(matrix, i)