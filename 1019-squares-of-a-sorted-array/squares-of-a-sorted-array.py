class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[0]*len(nums)
        l,r=0,len(nums)-1
        p=r
        while l<=r:
            left_square=nums[l]**2
            right_square=nums[r]**2
            if left_square<right_square:
                squares[p]=right_square
                r-=1
            else:
                squares[p]=left_square
                l+=1
            p-=1
        return squares
        