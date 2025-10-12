class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maxTravel=0
        # n=len(nums)
        # if n==1:
        #     return True #for this type of test case [0]
        # for i in range(n-1):
        #     if i>maxTravel:
        #         return False   #for this type testCase [0,2,3]
        #     maxTravel=max(maxTravel,i+nums[i])
        #     if maxTravel>=len(nums)-1:
        #         return True
        # return False

        #O(n) TC and O(1) Space Greedy
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        