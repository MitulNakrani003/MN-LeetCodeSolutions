class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Identify the first decreasing element when scanning the list from the right end.
        # Find the smallest element on the right side that is greater than this first decreasing element.
        # Swap these two elements.
        # Reverse the sublist starting from the now first decreasing element index to the end of the list.

        if len(nums) == 1:
            return

        i = len(nums) - 2
        while i != -1:
            if nums[i] < nums[i+1]:
                break
            i-=1
        
        if i == -1:
            nums.reverse()
            return

        print(i)

        x = len(nums) - 1
        while x > i:
            if nums[x] > nums[i]:
                break
            x-=1
        
        print(x)

        nums[x], nums[i] = nums[i], nums[x]


        print(nums)

        nums[i+1:] = reversed(nums[i+1:])




