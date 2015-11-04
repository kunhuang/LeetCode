class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        self.num_island = 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.bfs(i, j)
                    self.num_island += 1

        return self.num_island
    
    def dfs(self, i, j):
        self.grid[i][j] = 0
        for new_i, new_j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0<= new_i < self.m and 0 <= new_j < self.n and self.grid[new_i][new_j] == "1":
                self.dfs(new_i, new_j)

    def bfs(self, i, j):
        current_layer = [(i,j)]
        next_layer = []
        while len(current_layer) > 0:
            for (i, j) in current_layer:
                grid[i][j] = 0
                for new_i, new_j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= new_i < self.m and 0 <= new_j < self.n and self.grid[new_i][new_j] == "1":
                        next_layer.append((new_i, new_j))
            current_layer = next_layer[:]
            next_layer = []

grid = [
    ['0', '0', '1'],
    ['1', '0', '1'],
    ['1', '0', '1']
]
print Solution().numIslands(grid)