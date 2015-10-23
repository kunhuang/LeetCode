import pdb
class Range(object):
    """docstring for Range"""
    def __init__(self, row, col_start, col_end, surrounded, group_id):
        super(Range, self).__init__()
        self.row = row
        self.col_start = col_start
        self.col_end = col_end
        self.surrounded = surrounded
        self.group_id = group_id

class RangeGroup(object):
    """docstring for RangeGroup"""
    def __init__(self, new_range):
        super(RangeGroup, self).__init__()
        self.range_list = [new_range]
        self.surrounded = new_range.surrounded
        
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        range_list = []
        group_list = []
        range_list_last_row = []
        range_list_this_row = []
        for row_num, row in enumerate(board):
            # pdb.set_trace()
            # Tricky point: all element in the row is O
            col_start = None
            for col_num, ele in enumerate(row):
                if col_start is not None:
                    if ele == "O":
                        continue
                    else:
                        surrounded = not (row_num==0 or row_num==len(board)-1 or col_start == 0)
                        new_range = Range(row_num, col_start, col_num-1, surrounded, len(group_list))
                        group_list.append(RangeGroup(new_range))
                        for range_ in range_list_last_row:
                            if self.cover(new_range, range_) and range_.group_id != new_range.group_id:
                                # Tricky point: we range in same group might union here
                                self.group_union(group_list, range_.group_id, new_range.group_id)
                        range_list.append(new_range)
                        range_list_this_row.append(new_range)
                        col_start = None
                else:
                    if ele == "O":
                        col_start = col_num
                    else:
                        continue

            if col_start is not None:
                new_range = Range(row_num, col_start, len(row)-1, False, len(group_list))
                group_list.append(RangeGroup(new_range))
                for range_ in range_list_last_row:
                    if self.cover(new_range, range_):
                        self.group_union(group_list, range_.group_id, new_range.group_id)
                range_list.append(new_range)
                range_list_this_row.append(new_range)
                col_start = None
        
            range_list_last_row = range_list_this_row[:]
            range_list_this_row = []
    
        for range_ in range_list:
            if group_list[range_.group_id].surrounded == True:
                for i in range(range_.col_start, range_.col_end+1):
                    board[range_.row][i] = 'X'
    def cover(self, range1, range2):
        if range1.col_start > range2.col_end or range1.col_end < range2.col_start:
            return False
        return True

    def group_union(self, group_list, group_id1, group_id2):
        # Tricky point
        if group_id1 == group_id2:
            return 

        if len(group_list[group_id1].range_list) < len(group_list[group_id2].range_list):
            group_id2, group_id1 = group_id1, group_id2

        for range_ in group_list[group_id2].range_list:
            range_.group_id = group_id1
            group_list[group_id1].range_list.append(range_)

        if group_list[group_id2].surrounded == False:
            group_list[group_id1].surrounded = False

# map(lambda x: x.group_id, range_list)
board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["O","X","O","O"],
        ["X","O","X","X"]
        ]
board = [
        list("OXOOOOOOO"),
        list("OOOXOOOOX"),
        list("OXOXOOOOX"),
        list("OOOOXOOOO"),
        list("XOOOOOOOX"),
        list("XXOOXOXOX"),
        list("OOOXOOOOO"),
        list("OOOXOOOOO"),
        list("OOOOOXXOO")]

board = [
list("OOOOOOOO"),
list("OOOOXOOO"),
list("OXOOOOOO"),
list("OOOOOOOO"),
list("XOOXOOXO"),
list("OOOOOOOO"),
list("OOOOOOOO"),
list("OOOOOOOO")]

Solution().solve(board)
print board