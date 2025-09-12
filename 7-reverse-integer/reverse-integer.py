class Solution:
    def reverse(self, p: int) -> int:
        isNeg=False
        if p<0:
            isNeg=True
        p=abs(p)
        res=0
        while p:
            rem=p%10
            res=res*10+rem
            p=p//10
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        

        if res > INT_MAX or res < INT_MIN:
            return 0

        return -res if isNeg else res
        