class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        r = intervals[0][1]
        removal = 0
        for x in intervals[1:]:
            if x[0]<r:
                removal += 1
            else:
                r = x[1]
        return removal
            