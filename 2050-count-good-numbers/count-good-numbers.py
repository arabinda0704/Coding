class Solution:
    def myPow(self, x: int, n: int, mod: int) -> int:
        ans = 1
        while n:
            if n % 2:
                ans = (ans * x) % mod
            x = (x * x) % mod
            n //= 2
        return ans
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        odd=n//2
        even=n//2+n%2
        return (self.myPow(5,even,mod)*self.myPow(4,odd,mod))%mod

        