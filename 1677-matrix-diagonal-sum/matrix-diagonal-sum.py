class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    summ+=mat[i][j]
                if i == len(mat[0])-j - 1 and i != j:  
                    summ += mat[i][j]
        return summ
        