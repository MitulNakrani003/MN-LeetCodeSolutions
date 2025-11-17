class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = 0
        blue = len(nums)-1
        white = 0
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red+=1
                white+=1
            elif nums[white] == 2:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue-=1
            else:
                white+=1
            
        
            
            

        