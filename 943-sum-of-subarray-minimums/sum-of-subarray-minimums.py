class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #Brute Force ->This will give TLE
        # summ=0
        # MOD=10**9+7
        # for i in range(len(arr)):
        #     mini=arr[i]
        #     for j in range(i,len(arr)):
        #         mini=min(mini,arr[j])
        #         summ=(summ+mini)%MOD
        # return summ 

        #Optimal
        MOD = 10**9 + 7
        n = len(arr)

        # Compute previous smaller
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # Compute next smaller
        next_smaller = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        res = 0
        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller[i] - i
            res = (res + arr[i] * left * right) % MOD

        return res

    