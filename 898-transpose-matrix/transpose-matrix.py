class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        matrix1 = [[0] * rows for _ in range(cols)]  # correct shape

        for i in range(rows):
            for j in range(cols):
                matrix1[j][i] = matrix[i][j]

        return matrix1
