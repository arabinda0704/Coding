class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(m*n) TC and O(n) SC
        # dp = [1] * n
        # for i in range(m - 2, -1, -1):
        #     for j in range(n - 2, -1, -1):
        #         dp[j] += dp[j + 1]

        # return dp[0]
        
        # O(min(m,n)) TC and O(1) SC
        if m == 1 or n == 1:
            return 1
        if m < n:
            m, n = n, m

        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1

        return res
        