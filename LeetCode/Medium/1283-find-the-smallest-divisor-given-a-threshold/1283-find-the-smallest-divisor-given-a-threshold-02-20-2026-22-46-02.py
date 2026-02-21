class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def getDivisorSum(divisor):
            dividedArr = [math.ceil(x/divisor) for x in nums]
            return sum(dividedArr)
        
        print(getDivisorSum(4))

        def binSearch(left,right):
            mid = (left+right)//2
            if left == right:
                return left
            if getDivisorSum(mid) > threshold:
                return binSearch(mid+1,right)
            else:
                return binSearch(left,mid)
        
        # print(binSearch(left,right))
        return binSearch(left,right)
