class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Since it is a square matrix
        l,r=0,len(mat)-1
        while l<r:
            for i in range(r-l):
                top,bottom=l,r
                topLeft=mat[top][l+i]

                mat[top][l+i]=mat[bottom-i][l]
                mat[bottom-i][l]=mat[bottom][r-i]
                mat[bottom][r-i]=mat[top+i][r]
                mat[top+i][r]=topLeft

            l+=1
            r-=1
        