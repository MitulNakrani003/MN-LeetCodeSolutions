class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        result = [[] for _ in range(numRows)]
        # print(result)
        placement = 0
        direction = 1
        for x in s:
            result[placement].append(x)
            # print(result)
            if direction == 1 and placement == numRows-1:
                direction = -1
            elif direction == -1 and placement == 0:
                direction = 1
            
            if direction == 1:
                placement+=1
            else:
                placement-=1
        # print(result)
        result = ["".join(x) for x in result]
        
        return "".join(result)