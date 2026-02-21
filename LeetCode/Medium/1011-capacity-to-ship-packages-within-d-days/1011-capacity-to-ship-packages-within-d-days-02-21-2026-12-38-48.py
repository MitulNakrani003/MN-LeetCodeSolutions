class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = min(weights)
        right = sum(weights)

        def daysTake(capacity):
            currcapacity = capacity
            daystake = 0
            for i, x in enumerate(weights):
                if x <= currcapacity:
                    currcapacity-=x
                else:
                    print(x, currcapacity, i)
                    daystake +=1
                    currcapacity = capacity
                    currcapacity-=x
                    if currcapacity < 0:
                        return False
            if currcapacity < capacity:
                daystake+=1
            print(daystake)
            if daystake <= days:
                return True
            else:
                return False


        def binarySearch(left,right):
            mid = (left+right)//2
            if left == right:
                return left
            
            if daysTake(mid):
                return binarySearch(left,mid)
            else:
                return binarySearch(mid+1,right)
            
        return binarySearch(left,right)
        # return 0


            