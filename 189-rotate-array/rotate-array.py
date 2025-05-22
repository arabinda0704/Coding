def rev(nums,l,r):
    while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n=len(nums)
        k=k % n
        l,r=0,len(nums)-1
        rev(nums,0,n-1)
        rev(nums,0,k-1)
        rev(nums,k,n-1)
        