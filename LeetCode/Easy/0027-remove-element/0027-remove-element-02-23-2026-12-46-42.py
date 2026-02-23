class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        iteridx = 0
        while iteridx < len(nums):
            if nums[iteridx] != val:
                nums[curr],nums[iteridx] = nums[iteridx],nums[curr]
                curr+=1
                iteridx+=1
            else:
                iteridx+=1
        return curr
