class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        squares=defaultdict(set)
        n=9
        for i in range(n):
            for j in range(n):
                if board[i][j]==".":
                    continue
                elif board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[i//3,j//3]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[i//3,j//3].add(board[i][j])
        return True
