INF = 2**31 - 1

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms is None or len(rooms) == 0 or len(rooms[0]) == 0:
            return 

        m = len(rooms)
        n = len(rooms[0])
        
        current_layer = []
        next_layer = []
        layer_num = 0

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    current_layer.append((i, j))

        while len(current_layer) > 0:
            layer_num += 1
            for i, j in current_layer:
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= new_i < m and 0 <= new_j < n and rooms[new_i][new_j] == INF:
                        rooms[new_i][new_j] = layer_num
                        next_layer.append((new_i, new_j))

            current_layer = next_layer[:]
            next_layer = []

        return 


rooms = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]

Solution().wallsAndGates(rooms)
print rooms