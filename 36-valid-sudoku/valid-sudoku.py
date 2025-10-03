class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows=defaultdict(set)
        # cols=defaultdict(set)
        # squares=defaultdict(set)
        # n=9
        # for i in range(n):
        #     for j in range(n):
        #         if board[i][j]==".":
        #             continue
        #         elif board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[i//3,j//3]:
        #             return False
        #         else:
        #             rows[i].add(board[i][j])
        #             cols[j].add(board[i][j])
        #             squares[i//3,j//3].add(board[i][j])
        # return True

        #Another
        rows=defaultdict(set)
        cols=defaultdict(set)
        squares=defaultdict(set)
        n=9
        #1. Check Row and Column
        for i in range(n):
            for j in range(n):
                if board[i][j]==".":
                    continue
                elif board[i][j] in rows[i] or board[i][j] in cols[j]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
        # 2. Check 3x3 Box
        for i in range(n):
            for j in range(n):
                start_row, start_col = 3 * (i // 3), 3 * (j // 3)
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        if board[i][j]==".":
                            continue
                        elif board[i][j] in squares[r,c]:
                            return False
                        else:
                            squares[r,c].add(board[i][j])
        return True
