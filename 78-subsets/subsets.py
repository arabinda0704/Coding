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
        # res = []
        # subset = []
        # self.dfs(0,nums,subset,res)
        # return res
        res = []
        # nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            #     i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

