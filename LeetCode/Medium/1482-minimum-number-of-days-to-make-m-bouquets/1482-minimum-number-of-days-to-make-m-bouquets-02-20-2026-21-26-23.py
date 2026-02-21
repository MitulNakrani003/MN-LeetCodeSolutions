class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        
        def canBeDone(day):
            count = 0
            bouquetDone = 0
            for x in bloomDay:
                if x <= day:
                    count+=1
                else:
                    bouquetDone += int(count/k)
                    count = 0
            bouquetDone += int(count/k)
            return (bouquetDone >= m)

        def binarySearchVal(left,right):
            mid = (left+right)//2
            if left == right:
                return left
    
            if canBeDone(mid):
                return binarySearchVal(left,mid)
            else:
                return binarySearchVal(mid+1,right)
        
        temp = binarySearchVal(min(bloomDay),max(bloomDay))
        print(temp)
        return temp
