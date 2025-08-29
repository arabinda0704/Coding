class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left,right=0,len(matrix[0])-1
        top,buttom=0,len(matrix)-1
        while left<=right and top<=buttom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,buttom+1):
                res.append(matrix[i][right])
            right-=1

            if not (left<=right and top<=buttom):
                break

            for i in range(right,left-1,-1):
                res.append(matrix[buttom][i])
            buttom-=1
            for i in range(buttom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        return res
        