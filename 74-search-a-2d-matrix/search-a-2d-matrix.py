class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        i=0
        j=ROWS*COLS-1
        while i<=j:
            mid=(i+j)//2
            if matrix[mid//COLS][mid%COLS]==target:
                return True
            elif matrix[mid//COLS][mid%COLS]<target:
                i=mid+1
            else:
                j=mid-1
        return False