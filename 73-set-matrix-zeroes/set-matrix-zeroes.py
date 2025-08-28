class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(m+n) Space
        # ROWS, COLS = len(matrix),len(matrix[0])
        # rows,cols=[0]*ROWS,[0]*COLS
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j]==0:
        #             rows[i]=1
        #             cols[j]=1
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if rows[i] or cols[j]:
        #             matrix[i][j]=0


        #Better/Optimal with O(1) space or Inplace
        ROWS,COLS=len(matrix),len(matrix[0])
        rowZero=False
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        rowZero=True
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        for i in range(ROWS):
            if matrix[0][0]==0:
                matrix[i][0]=0
        for j in range(COLS):
            if rowZero:
                matrix[0][j]=0

        

            