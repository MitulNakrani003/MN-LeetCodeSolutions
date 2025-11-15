class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])
        for x in range(1,numRows):
            leftpointer = -1
            rightpointer = leftpointer + 1
            thisresult = []
            n = len(result[x-1])
            iterarr = result[x-1]
            while rightpointer != n + 1:
                if leftpointer == -1:
                    thisresult.append(iterarr[rightpointer])
                elif leftpointer == n - 1:
                    thisresult.append(iterarr[leftpointer])
                else:
                    thisresult.append(iterarr[leftpointer]+iterarr[rightpointer])
                leftpointer+=1
                rightpointer+=1
            result.append(thisresult)
        return result