class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # insert_pos=1
        # for i in range(1,len(nums)):
        #     if nums[i]!=nums[i-1]:
        #         nums[insert_pos]=nums[i]
        #         insert_pos+=1
        # return insert_pos
        l = 0
        for num in nums:
            if l < 1 or num != nums[l - 1]:
                nums[l] = num
                l += 1
        return l
        