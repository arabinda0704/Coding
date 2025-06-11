class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        #Brute Force will give Time Limit Exceeded
        # res=0
        # for i in range(len(nums)):
        #     for j in range(len(nums)-1,i,-1):
        #         if nums[j]>=nums[i]:
        #             res=max(res,j-i)
        #             break            
        # return res

        #Optimal
        maxRight=[None]*len(nums)#fill it initially with 0 or None
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                maxRight[i]=nums[i]
            else:
                maxRight[i]=max(nums[i],maxRight[i+1])
        l=0
        res=0
        for r in range(len(nums)):
            if nums[l]>maxRight[r]:
                l+=1
            res=max(res,r-l)
        return res


        