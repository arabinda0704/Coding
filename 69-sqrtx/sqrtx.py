class Solution:
    def mySqrt(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            mid=(l+r)//2
            if mid*mid==n:
                return mid
            elif mid*mid<n:
                l=mid+1
            else:
                r=mid-1
        return r