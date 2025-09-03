class Solution:
    def mySqrt(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            mid=l+(r-l)//2
            if mid*mid==n:
                return mid
            elif mid*mid>n:
                r=mid-1
            else:
                l=mid+1
        return r