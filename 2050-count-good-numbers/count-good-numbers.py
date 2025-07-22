class Solution:
    # def myPow(self, x: int, n: int, mod: int) -> int:
    #     ans = 1
    #     while n:
    #         if n % 2:
    #             ans = (ans * x) % mod
    #         x = (x * x) % mod
    #         n //= 2
    #     return ans


        #Using recurssion

        

    def countGoodNumbers(self, n: int) -> int:
        def helper(x,n,mod):
            if x==0:return 0
            if n==0:return 1

            res=helper(x,n//2,mod)
            res=res*res
            res%=mod
            return res*x if n%2 else res
        mod = 10**9 + 7
        odd=n//2
        even=n//2+n%2
        return (helper(5,even,mod)*helper(4,odd,mod))%mod

        