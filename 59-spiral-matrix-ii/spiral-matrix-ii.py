class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        left,right=0,n-1
        top,buttom=0,n-1
        num=1
        while left<=right and top<=buttom:
            for i in range(left,right+1):
                matrix[top][i]=num
                num+=1
            top+=1
            for i in range(top,buttom+1):
                matrix[i][right]=num
                num+=1
            right-=1

            if not (left<=right and top<=buttom):
                break

            for i in range(right,left-1,-1):
                matrix[buttom][i]=num
                num+=1
            buttom-=1
            for i in range(buttom,top-1,-1):
                matrix[i][left]=num
                num+=1
            left+=1
        return matrix
        