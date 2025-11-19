class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        firstidx = 0
        lastidx = len(matrix) - 1
        if firstidx != lastidx:
            while True: 
                if firstidx+1 == lastidx:
                    if target >= matrix[lastidx][0] and lastidx == len(matrix)-1:
                        firstidx += 1
                    break
                mididx = int((firstidx + lastidx)/2)
                if target >= matrix[mididx][0]:
                    firstidx = mididx
                else:
                    lastidx = mididx
        
        print(firstidx)
        ourarr = matrix[firstidx]
        start = 0
        end = len(ourarr)-1
        mid = int((start + end)/2)
        if len(ourarr) == 1:
            if ourarr[0] == target:
                return True
            else:
                return False
        while True:
            if ourarr[mid] == target:
                return True
            if start+1 == end:
                if ourarr[start] == target or ourarr[end] == target:
                    return True
                else:
                    return False
            mid = int((start + end)/2)
            if target > ourarr[mid]:
                start = mid
            else:
                end = mid
