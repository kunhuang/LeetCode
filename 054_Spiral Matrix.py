import pdb
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []

        layer = min(m/2, n/2)
        layer_i = 0

        while layer_i < layer:
            # pdb.set_trace()
            for i in range(layer_i, n-layer_i-1):
                result.append(matrix[layer_i][i])
            for i in range(layer_i, m-layer_i-1):
                result.append(matrix[i][n-layer_i-1])
            for i in range(n-layer_i-1, layer_i, -1):
                result.append(matrix[m-layer_i-1][i])
            for i in range(m-layer_i-1, layer_i, -1):
                result.append(matrix[i][layer_i])
            layer_i += 1
        if m > n and n%2:
            for i in range(layer, m-layer):
                result.append(matrix[i][layer])
        if m < n and m%2:
            for i in range(layer, n-layer):
                result.append(matrix[layer][i])
        if m == n and m%2:
            result.append(matrix[layer][layer])
        return result

matrix = [[1, 2]]

print Solution().spiralOrder(matrix)
                