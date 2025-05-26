class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        ans=0
        
        while left <= right:
            mid = (left + right) // 2
            summ = 0
            for i in range(len(nums)):
                summ+=math.ceil(nums[i]/mid)
            if summ > threshold:
                left = mid + 1
            else:
                ans=mid
                right = mid-1
        return ans
        
            