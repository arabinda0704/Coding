class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l=m=0
        oddCount=0
        res=0
        for r in range(len(nums)):
            if nums[r] & 1:
                oddCount+=1

            while oddCount>k:
                if nums[l] & 1:
                    oddCount-=1
                l+=1   
                m=l 
            if oddCount==k:
                while not (nums[m] & 1):
                    m+=1
                res+=(m-l+1)
                   
        return res
                    