class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res,[], nums, [False] * len(nums))
        return res

    def backtrack(self,res : List[List[int]], perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(res,perm, nums, pick)
                perm.pop()
                pick[i] = False