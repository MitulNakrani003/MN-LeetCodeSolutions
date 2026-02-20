class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums.insert(0,float('-inf'))
        nums.append(float('-inf'))
        def binsearch(left,right):
            mid = (left + right)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid] and nums[mid] <= nums[mid+1]:
                return binsearch(mid,right)
            else:
                return binsearch(left,mid)
        return binsearch(0,len(nums)-1)-1