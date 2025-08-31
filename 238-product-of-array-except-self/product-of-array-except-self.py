class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCnt=0
        prod=1
        res=[0]*len(nums)
        for num in nums:
            if num==0:
                zeroCnt+=1
            else:
                prod*=num
        if zeroCnt>1:
            return res
        for i in range(len(nums)):
            if zeroCnt==1:
                if nums[i] !=0:
                    res[i]=0
                else:
                    res[i]=prod
            else:
                res[i]=prod//nums[i]
        return res
        