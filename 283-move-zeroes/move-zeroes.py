class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0

        # Step 2: Go through each number in the list
        for i in range(len(nums)):
            if nums[i] != 0:
                # Place the non-zero number at the front
                nums[count] = nums[i]
                count += 1

        # Step 3: After placing all non-zero numbers at the beginning,
        # fill the rest of the list with zeros
        for i in range(count, len(nums)):
            nums[i] = 0
        