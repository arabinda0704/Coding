class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ans=0
        # for i in nums:
        #     ans^=i
        # return ans
        #Another
        # dict1 = defaultdict(int)  # default value for any key is 0

        # for i in range(len(nums)):
        #     dict1[nums[i]] += 1
        # for i in range(len(nums)):
        #     if dict1[nums[i]]==1:
        #         return nums[i]

        #Another
        from collections import Counter

        dict1 = Counter(nums)
        for i in range(len(nums)):
            if dict1[nums[i]]==1:
                return nums[i]


                