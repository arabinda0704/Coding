# class Solution:
#     def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
#         MOD = 12345
#         m, n = len(grid), len(grid[0])
#         arr = [grid[i][j] for i in range(m) for j in range(n)]
#         size = len(arr)
        
#         # Step 1: Prefix and suffix product under modulo
#         prefix = [1] * size
#         suffix = [1] * size
        
#         for i in range(1, size):
#             prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        
#         for i in range(size - 2, -1, -1):
#             suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
        
#         # Step 2: Construct result array
#         result = [(prefix[i] * suffix[i]) % MOD for i in range(size)]
        
#         # Step 3: Convert back to 2D matrix
#         ans = []
#         idx = 0
#         for i in range(m):
#             ans.append(result[idx:idx + n])
#             idx += n
        
#         return ans

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m = len(grid)
        n = len(grid[0]) if m else 0

        # Flatten grid to 1D array
        arr = [grid[i][j] for i in range(m) for j in range(n)]
        size = len(arr)

        if size == 0:
            return []

        # prefix[i] = product of arr[0..i-1] % MOD
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * (arr[i-1] % MOD)) % MOD

        # suffix[i] = product of arr[i+1..size-1] % MOD
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * (arr[i+1] % MOD)) % MOD

        # result for flattened array: product of all except arr[i]
        result_flat = [(prefix[i] * suffix[i]) % MOD for i in range(size)]

        # convert back to m x n matrix
        ans = []
        idx = 0
        for i in range(m):
            ans.append(result_flat[idx:idx + n])
            idx += n

        return ans

        