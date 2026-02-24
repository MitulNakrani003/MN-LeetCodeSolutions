class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binarysearch(left,right):
            if left>right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if left == right:
                return -1

            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    return binarysearch(left,mid-1)
                else:
                    return binarysearch(mid+1,right)
            else:
                if target > nums[mid] and target <= nums[right]:
                    return binarysearch(mid+1,right)
                else:
                    return binarysearch(left,mid-1)
        t = binarysearch(0,len(nums)-1)
        if nums[t] == target:
            return t
        else:
            return -1
                
                