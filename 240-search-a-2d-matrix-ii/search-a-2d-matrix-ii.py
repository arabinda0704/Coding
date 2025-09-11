class Solution:
    def bs(self,arr,target):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                r=mid-1
            else:
                l+=1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if self.bs(matrix[i],target):
                return True
        return False
        