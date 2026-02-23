class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        
        left = max(nums)
        right = sum(nums)
        
        def canDoItinKWithMaxVal(value):
            count = 0
            currsum = 0
            for x in nums:
                if currsum + x <= value:
                    currsum+=x
                else:
                    count+=1
                    currsum = x
            if currsum > 0 and currsum <= value:
                count+=1
            # print(count)
            if count <= k:
                return True
            else:
                return False
        
        print(canDoItinKWithMaxVal(5))

        print(left,right)
        def binarysearch(left,right):
            mid = (left+right)//2
            if left == right:
                return left
            
            if canDoItinKWithMaxVal(mid):
                return binarysearch(left,mid)
            else:
                return binarysearch(mid+1,right)
        
        return binarysearch(left,right)
        # return 0
