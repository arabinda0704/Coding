from typing import List

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()   # sort once to handle duplicates

        def dfs(i, cur, target):
            if target == 0:
                res.append(cur[:])   # found a valid combination
                return
            if target < 0:
                return

            for j in range(i, len(nums)):
                # \U0001f511 skip duplicates
                if j > i and nums[j] == nums[j-1]:
                    continue
                # prune if number exceeds target
                if nums[j] > target:
                    break

                cur.append(nums[j])
                dfs(j+1, cur, target - nums[j])  # move forward
                cur.pop()

        dfs(0, [], target)
        return res
