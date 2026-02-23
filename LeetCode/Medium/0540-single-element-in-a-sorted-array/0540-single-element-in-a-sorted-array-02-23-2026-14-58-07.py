class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def binarysearch(left,right):
            mid = (left+right)//2
            if left == right:
                return left
            
            if mid % 2 == 1:
                mid-=1
            
            if nums[mid] == nums[mid+1]:
                return binarysearch(mid+2,right)
            else:
                return binarysearch(left,mid)
            
                
        t = binarysearch(0,len(nums)-1)
        print(t)
        return nums[t]
