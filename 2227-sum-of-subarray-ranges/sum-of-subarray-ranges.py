class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #Brute Force
        sum=0
        for i in range(len(nums)):
            mini=maxi=nums[i]
            for j in range(i+1,len(nums)):
                mini=min(nums[j],mini)
                maxi=max(maxi,nums[j])
                sum+=(maxi-mini)
        return sum

        