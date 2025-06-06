class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if len(nums) <= 2:
        #     return len(nums)
        
        # insert_pos = 2
        # for i in range(2, len(nums)):
        #     # Compare current number with the element two positions before
        #     if nums[i] != nums[insert_pos - 2]:
        #         nums[insert_pos] = nums[i]
        #         insert_pos += 1
        # return insert_pos
        l = 0
        for num in nums:
            if l < 2 or num != nums[l - 2]:
                nums[l] = num
                l += 1
        return l
