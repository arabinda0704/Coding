class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur,target):
            if target == 0:
                res.append(cur.copy())
                return
            
            if i>=len(nums) or target<0:
                return
            cur.append(nums[i])
            dfs(i,cur,target-nums[i])
            cur.pop()
            dfs(i+1,cur,target)

        
        dfs(0, [],target)
        return res