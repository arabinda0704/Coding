class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix),len(matrix[0])
        rows,cols=[0]*ROWS,[0]*COLS
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]==0:
                    rows[i]=1
                    cols[j]=1
        for i in range(ROWS):
            for j in range(COLS):
                if rows[i] or cols[j]:
                    matrix[i][j]=0
            