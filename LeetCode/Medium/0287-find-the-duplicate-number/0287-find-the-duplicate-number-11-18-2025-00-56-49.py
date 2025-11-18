class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        currptr = 0
        while True:
            temp = currptr
            currptr = nums[currptr] 
            nums[temp] = 0
            if nums[currptr] == 0:
                return currptr
            
            