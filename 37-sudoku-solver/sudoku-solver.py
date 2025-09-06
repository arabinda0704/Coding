from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Pre-fill sets with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)
                else:
                    empties.append((i, j))
        k=0
        def backtrack(k):
            if k == len(empties):
                return True  # solved

            i, j = empties[k]
            b = (i // 3) * 3 + j // 3

            for c in "123456789":
                if c not in rows[i] and c not in cols[j] and c not in boxes[b]:
                    board[i][j] = c
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[b].add(c)

                    if backtrack(k + 1):
                        return True

                    # undo choice
                    board[i][j] = "."
                    rows[i].remove(c)
                    cols[j].remove(c)
                    boxes[b].remove(c)

            return False

        backtrack(k)
