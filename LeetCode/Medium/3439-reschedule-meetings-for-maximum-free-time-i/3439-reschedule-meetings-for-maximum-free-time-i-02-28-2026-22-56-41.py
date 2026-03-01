class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        gaps.append(startTime[0])
        for i in range(1,len(startTime)):
            gaps.append(startTime[i]-endTime[i-1])
        gaps.append(eventTime-endTime[-1])
        print(gaps)
        windowsize = k+1
        windowleft = 0
        sumgap = sum(gaps[:windowsize])
        maxgap = sumgap
        windowright = k
        while windowright < len(gaps)-1:
            windowright+=1
            sumgap+=gaps[windowright]
            sumgap-=gaps[windowleft]
            windowleft+=1
            maxgap = max(sumgap,maxgap)
        return maxgap

            

