class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # l=m=0
        # oddCount=0
        # res=0
        # for r in range(len(nums)):
        #     if nums[r] & 1:
        #         oddCount+=1

        #     while oddCount>k:
        #         if nums[l] & 1:
        #             oddCount-=1
        #         l+=1   
        #         m=l 
        #     if oddCount==k:
        #         while not (nums[m] & 1):
        #             m+=1
        #         res+=(m-l+1)
                   
        # return res

        #One More Solution
        n=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i] & 1:
                n[i]=1
        def helper(x):
            if x < 0:
                return 0
            res = l = cur = 0
            for r in range(len(n)):
                cur += n[r]
                while cur > x:
                    cur -= n[l]
                    l += 1
                res += (r - l + 1)
            return res

        return helper(k) - helper(k - 1)
                    