import pdb
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        length = 9
        empty_hash_table = dict(zip(list("123456789"), [False]*length))
        hash_table = empty_hash_table.copy()
        for _board in [board, [[row[i] for row in board] for i in range(length)]]:
            for row in _board:
                for item in row:
                    # pdb.set_trace()
                    if item == '.':
                        continue
                    if hash_table[item]:
                        return False
                    hash_table[item] = True
                hash_table = empty_hash_table.copy()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        item = board[3*i+k][3*j+l]
                        if item == '.':
                            continue
                        if hash_table[item]:
                            return False
                        hash_table[item] = True
                hash_table = empty_hash_table.copy()
        return True
print Solution().isValidSudoku([".87654321","2.8......","3........","4........","5........","6........","7........","8........","9........"])