class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a=nums[i]
            l=i+1
            r=n-1
            while l<r:
                if a+nums[l]+nums[r]==0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif a+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
                    
        return res


        