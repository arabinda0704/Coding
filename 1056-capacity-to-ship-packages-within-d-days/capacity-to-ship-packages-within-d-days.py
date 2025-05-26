class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        ans=0
        while l<=r:
            mid=(l+r)//2
            cnt = 1 
            summ = 0
            
            for w in weights:
                if summ + w > mid:
                    cnt += 1
                    summ = 0
                summ += w
            if cnt<=days:
                ans=mid
                r=mid-1
            else:
                l=mid+1
                    
        return ans