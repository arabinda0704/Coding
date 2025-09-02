class Solution:
    def trap(self, height: List[int]) -> int:
        #Most optimal way O(N) TC
        n=len(height)
        res=0
        l,r=0,n-1
        leftMax,rightMax=height[l],height[r]
        while l<r:
            if height[l]<height[r]:
                l+=1
                leftMax=max(leftMax,height[l])
                res+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax,height[r])
                res+=rightMax-height[r]
        return res