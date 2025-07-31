class Solution:
    def dfs(self,i,nums,subset,res):
        if i >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        self.dfs(i + 1,nums,subset,res)
        subset.pop()
        self.dfs(i + 1,nums,subset,res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        self.dfs(0,nums,subset,res)
        return res

