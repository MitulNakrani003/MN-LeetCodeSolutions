class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prefix = [[0]*n for x in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    prefix[i][j] = 0
                else:
                    prefix[i][j] = int(prefix[i-1][j])+1 if i > 0 else 1

        def maxRect(histogram):
            monotonicstack = []
            maxarea = 0
            for i in range(len(histogram)):
                while monotonicstack and histogram[monotonicstack[-1]] > histogram[i]:
                    height = histogram[monotonicstack[-1]]
                    next_low_index = i
                    prev_low_index = monotonicstack[-2] if len(monotonicstack)>1 else -1
                    area = height * (next_low_index - prev_low_index - 1)
                    maxarea = max(maxarea, area)
                    monotonicstack.pop()
                monotonicstack.append(i)
            while monotonicstack:
                height = histogram[monotonicstack[-1]]
                next_low_index = len(histogram)
                prev_low_index = monotonicstack[-2] if len(monotonicstack)>1 else -1
                area = height * (next_low_index - prev_low_index - 1)
                maxarea = max(maxarea, area)
                monotonicstack.pop()
            return maxarea
        
        finalmax = 0
        for x in prefix:
            t = maxRect(x)
            print(t)
            finalmax = max(finalmax, t)
        
        return finalmax



        