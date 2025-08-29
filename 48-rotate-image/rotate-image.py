class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Since it is a square matrix
        # l,r=0,len(mat)-1
        # while l<r:
        #     for i in range(r-l):
        #         top,bottom=l,r
        #         topLeft=mat[top][l+i]

        #         mat[top][l+i]=mat[bottom-i][l]
        #         mat[bottom-i][l]=mat[bottom][r-i]
        #         mat[bottom][r-i]=mat[top+i][r]
        #         mat[top+i][r]=topLeft

        #     l+=1
        #     r-=1
        
        #Another by Transposing
        n = len(mat)
        # transposing the matrix
        for i in range(n-1):
            for j in range(i+1,n):
                mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
        # reversing each row of the matrix
        for i in range(n):
            mat[i].reverse()