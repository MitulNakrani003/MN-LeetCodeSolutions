class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        increasingStack = []
        maxarea = 0
        for i in range(len(heights)):
            while increasingStack and heights[increasingStack[-1]] > heights[i]:
                currval = heights[increasingStack[-1]]
                curr_nseval = heights[i]
                nseindex = i 
                curr_pseval = heights[increasingStack[-2]] if len(increasingStack)>1 else -1
                pseindex = increasingStack[-2] if len(increasingStack)>1 else -1
                maxarea = max(maxarea, currval * (nseindex - pseindex - 1))
                # print(currval, curr_nseval, curr_pseval, maxarea)
                increasingStack.pop()
            increasingStack.append(i)
        while increasingStack:
            currval = heights[increasingStack[-1]]
            nseindex = len(heights)
            curr_pseval = heights[increasingStack[-2]] if len(increasingStack)>1 else -1
            pseindex = increasingStack[-2] if len(increasingStack)>1 else -1
            maxarea = max(maxarea, currval * (nseindex - pseindex - 1))
            # print(currval, curr_nseval, curr_pseval, maxarea)
            increasingStack.pop()
        return maxarea




