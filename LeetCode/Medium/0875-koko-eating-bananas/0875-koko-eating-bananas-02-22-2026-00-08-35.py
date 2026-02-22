class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def canEatInH(rate):
            count = 0
            for x in piles:
                count += math.ceil(x/rate)
            if count <= h:
                return True
            else:
                return False
        
        # print(canEatInH(22))

        def binarysearch(left,right):
            mid = (left+right)//2
            if left == right:
                return left
            
            if canEatInH(mid):
                return binarysearch(left,mid)
            else:
                return binarysearch(mid+1,right)
        
        return binarysearch(l,r)
        # return 0
                