class Solution:
    def fib(self, n: int) -> int:
        # Tabular(Bottom-Up)
        # if n <= 1:
        #     return n
        # dp = [0] * (n+1)#n+1 because starts from 0th fibo or 0th ind
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        #Memoization(Top-Down)
        memo=[-1]*(n+1)
        def helper(k):
            # Base case
            if k <= 1:
                return k
            # Return from memo if already calculated
            if memo[k] != -1:
                return memo[k]
            # Recursive calculation + store in memo
            memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]

        return helper(n)

        