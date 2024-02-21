class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #part 1: iterating through rows
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        mini_grids = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in columns[c]:
                    return False
                index_x = r/3
                index_y = c/3
                if board[r][c] in mini_grids[index_x, index_y]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                mini_grids[(index_x, index_y)].add(board[r][c])
        return True
        