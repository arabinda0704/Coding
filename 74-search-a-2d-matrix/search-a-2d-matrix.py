class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Most Optimal O(log(m*n))
        # ROWS,COLS=len(matrix),len(matrix[0])
        # i=0
        # j=ROWS*COLS-1
        # while i<=j:
        #     mid=(i+j)//2
        #     if matrix[mid//COLS][mid%COLS]==target:
        #         return True
        #     elif matrix[mid//COLS][mid%COLS]<target:
        #         i=mid+1
        #     else:
        #         j=mid-1
        # return False

        # Same code for better understanding
        n = len(matrix)
        m = len(matrix[0])

        # apply binary search:
        low = 0
        high = n * m - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
