from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()  # use set to avoid duplicates
        self.backtrack(res, [], nums, [False] * len(nums))
        return [list(p) for p in res]  # convert tuples back to lists

    def backtrack(self, res: set, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            res.add(tuple(perm))  # store tuple (hashable)
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(res, perm, nums, pick)
                perm.pop()
                pick[i] = False
