class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Extreme Brute Force
        # res=[]
        # for i in range (len(nums)):
        #     nextGreater=-1
        #     flag=True
        #     for j in range(i+1,len(nums)):
        #         if nums[j] > nums[i]:
        #             flag=False
        #             nextGreater=nums[j]
        #             break
        #     if nextGreater==-1 and flag:
        #         for j in range(0,i):
        #             if nums[j] > nums[i]:
        #                 nextGreater=nums[j]   
        #                 break
        #     res.append(nextGreater)
        # return res

        # Better
        # res=[]
        # n=len(nums)
        # for i in range(n):
        #     nextGreater=-1
        #     for j in range (i+1,i+n):
        #         ind=j%n   
        #         if nums[ind] > nums[i]:
        #                 nextGreater=nums[ind]
        #                 break
        #     res.append(nextGreater)
        # return res

        #Optimal
        n = len(nums)
        nge = [-1] * n
        st = []


        for i in range(2 * n - 1, -1, -1):
            while st and st[-1] <= nums[i % n]:
                st.pop()


            if i < n:
                if st:
                    nge[i] = st[-1]
            st.append(nums[i % n])
        return nge





