class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        curr = 0
        while curr < len(intervals) and intervals[curr][1] < newInterval[0]:
            result.append(intervals[curr])
            curr += 1
        
        merged = newInterval
        while curr < len(intervals) and intervals[curr][0] <= newInterval[1]:
            merged = [min(merged[0], intervals[curr][0]),
                      max(merged[1], intervals[curr][1])]
            curr += 1
        result.append(merged)
        
        while curr < len(intervals):
            result.append(intervals[curr])
            curr += 1
        return result