class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = n-1-1
        while i > -1 and nums[i] >= nums[i+1]:
            i-=1
        print(i)
        if i == -1:
            nums.reverse()
            return
        minindex = i+1
        minval = nums[i+1]
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                if nums[j] <= minval:
                    minval = nums[j]
                    minindex = j
        nums[i],nums[minindex]=nums[minindex],nums[i]
        print(nums, i)
        left = i+1
        right = n-1
        print(left,right)
        while left<right:
            print("eyyy")
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        