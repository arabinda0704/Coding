class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            a=nums[i]
            if a==nums[i-1]and i>0:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threeSome=a+nums[l]+nums[r]
                if threeSome>0:
                    r-=1
                elif threeSome<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

                