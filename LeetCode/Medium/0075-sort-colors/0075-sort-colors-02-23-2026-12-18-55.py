class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for x in nums:
            if x == 0:
                zeros+=1
            elif x == 1:
                ones+=1
            else:
                twos+=1
        curr = 0
        while curr < len(nums):
            if zeros:
                nums[curr] = 0
                zeros-=1
            elif ones:
                nums[curr] = 1
                ones-=1
            else:
                nums[curr] = 2
                twos-=1
            curr+=1