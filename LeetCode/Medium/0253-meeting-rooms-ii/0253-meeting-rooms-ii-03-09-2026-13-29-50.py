class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startarr = sorted([i[0] for i in intervals])
        endarr = sorted([i[1] for i in intervals])
        res, maxcount = 0, 0
        i, j = 0, 0
        while i < len(startarr):
            if startarr[i]<endarr[j]:
                res+=1
                i+=1
            else:
                res-=1
                j+=1
            maxcount = max(maxcount, res)
        return maxcount