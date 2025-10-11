from typing import List

class Solution:
    def dfs(self, i, cur, target, res, nums):
        if target == 0:
            res.append(cur[:])
            return
        
        if i == len(nums) or target < 0:
            return
        
        # include current number
        cur.append(nums[i])
        self.dfs(i + 1, cur, target - nums[i], res, nums)
        cur.pop()

        # skip all duplicates of nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        
        # exclude current number
        self.dfs(i + 1, cur, target, res, nums)
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(0, [],target,res,nums)
        return res
