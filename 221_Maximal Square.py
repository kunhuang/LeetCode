class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
            
        m = len(matrix)
        n = len(matrix[0])

        max_square = [[0]*n for i in range(m)]

        max_space = 0
        
        for i in range(m):
            max_square[i][0] = 1 if matrix[i][0] == '1' else 0
            if max_space < max_square[i][0]:
                max_space = max_square[i][0]
        for j in range(1, n):
            max_square[0][j] = 1 if matrix[0][j] == '1' else 0
            if max_space < max_square[0][j]:
                max_space = max_square[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    max_square[i][j] = min(max_square[i-1][j-1], max_square[i-1][j], max_square[i][j-1])+1
                    if max_space < max_square[i][j]:
                        max_space = max_square[i][j]
        return max_space**2

matrix = [
"1001",
"1011",
"1111"
]
print Solution().maximalSquare(matrix)
