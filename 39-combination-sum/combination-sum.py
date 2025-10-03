class Solution:
    def dfs(self,i, cur,target,res,nums):
            if target == 0:
                res.append(cur.copy())
                return
            
            if i>=len(nums) or target<0:
                return
            cur.append(nums[i])
            self.dfs(i,cur,target-nums[i],res,nums)
            cur.pop()
            self.dfs(i+1,cur,target,res,nums)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0, [],target,res,nums)
        return res