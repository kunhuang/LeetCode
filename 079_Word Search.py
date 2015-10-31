class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board

        if word is None or word == '':
            return True

        if board == None or len(board)==0 or len(board[0]) == 0:
            return False

        self.used = []
        for i in range(len(board)):
            self.used.append([False]*len(board[0]))

        roots = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    roots.append((i, j))

        if len(roots) == 0:
            return False

        for i, j in roots:
            self.used[i][j] = True
            if self.dfs((i, j), word[1:]):
                return True
            self.used[i][j] = False
        return False

    def dfs(self, root, word):
        if word == '':
            return True
        i, j = root
        for (new_i, new_j) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if (0 <= new_i < len(self.board) and 
                0 <= new_j < len(self.board[0]) and 
                self.used[new_i][new_j] == False and 
                self.board[new_i][new_j]==word[0]):
                
                self.used[new_i][new_j] = True
                if self.dfs((new_i, new_j), word[1:]) == True:
                    return True
                self.used[new_i][new_j] = False
        return False

board = [
  ['A','A']
  # ,'C','E'],
  # ['S','F','C','S'],
  # ['A','D','E','E']
]
print Solution().exist(board, "AAA")