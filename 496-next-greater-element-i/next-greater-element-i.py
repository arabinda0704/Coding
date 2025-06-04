class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res=[]
        # for num in nums1:
        #     nextGreater=-1
        #     for i in range(len(nums2)-1,-1,-1):
        #         if nums2[i]>num:
        #             nextGreater=nums2[i]
        #         elif nums2[i]==num:
        #             break
        #     res.append(nextGreater)
        # return res
        nums1Idx = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res
