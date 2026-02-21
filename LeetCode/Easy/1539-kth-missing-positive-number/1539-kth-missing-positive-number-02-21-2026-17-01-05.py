class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        if k > (arr[-1] - len(arr)):
            return arr[-1] + (k - (arr[-1] - len(arr)))

        def binarySearch(lidx,ridx):
            mididx = (lidx+ridx)//2
            midval = arr[mididx]
            if lidx > ridx:
                return lidx
            
            if (midval-(mididx+1)) < k:
                return binarySearch(mididx+1,ridx)
            else:
                return binarySearch(lidx,mididx-1)
        
        temp = binarySearch(0,len(arr)-1)
        print(temp)
        temp-=1
        addthis = k-(arr[temp]-(temp+1))
        return arr[temp]+addthis