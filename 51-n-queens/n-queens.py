class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # ans=[]
        # rows=set()
        # negDiag=set() #r-c
        # posDiag=set() #r+c

        # board=[["."]*n for _ in range(n)]

        # def backtrack(c):
        #     if c==n:
        #         copy=["".join(col) for col in board]
        #         ans.append(copy)
        #     for r in range(n):
        #         if r in rows or r+c in posDiag or r-c in negDiag:
        #             continue
        #         rows.add(r)
        #         posDiag.add(r+c)
        #         negDiag.add(r-c)
        #         board[r][c]="Q"

        #         backtrack(c+1)

        #         rows.remove(r)
        #         posDiag.remove(r+c)
        #         negDiag.remove(r-c)
        #         board[r][c]="."
        # backtrack(0)
        # return ans

        # Same in a different way
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
