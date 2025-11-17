class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:\

        def getOverlap(lap1,lap2):
            left1 = lap1[0]
            left2 = lap2[0]
            right1 = lap1[1]
            right2 = lap2[1]
            result = [0,0]
            isOverlap = False
            if left2 < left1 and (right2 >= left1 and right2 <= right1):
                isOverlap = True
                result = [left2,right1]
            elif right2 > right1 and (left2 >= left1 and left2 <= right1):
                isOverlap = True
                result = [left1,right2]
            elif left2 < left1 and right2 > right1:
                isOverlap = True
                result = [left2,right2]
            elif left1 == left2 and right1 == right2:
                isOverlap = True
                result = [left1,right1]
            else:
                result = [left1, right1]
            return isOverlap, result

        intervals.sort(key=lambda x: x[0])
        i = 0
        j = 1
        while j < len(intervals):
            isOverlap, newInterval = getOverlap(intervals[i], intervals[j])
            if isOverlap:
                intervals[i] = newInterval
                del intervals[j]
            else:
                i+=1
                j+=1

        return intervals
        
         
            