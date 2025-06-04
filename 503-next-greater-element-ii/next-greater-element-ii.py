class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range (len(nums)):
            nextGreater=-1
            flag=True
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    flag=False
                    nextGreater=nums[j]
                    break
            if nextGreater==-1 and flag:
                for j in range(0,i):
                    if nums[j] > nums[i]:
                        nextGreater=nums[j]   
                        break
            res.append(nextGreater)
        return res