class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l,r=0,len(nums)-1
        # ans=nums[0]
        # while l<=r:
        #     mid=l+(r-l)//2
        #     if nums[mid]>=nums[l]:
        #         ans=min(ans,nums[l])
        #         l=mid+1
        #     else:
        #         ans=min(ans,nums[mid])
        #         r=mid-1
        # return ans
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:               # nums[mid] == nums[r]
                r -= 1
        return nums[l]
            


        