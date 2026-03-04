class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        curr = 0

        while curr < len(nums):
            if nums[curr] != 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                l+=1
            curr+=1
        return nums