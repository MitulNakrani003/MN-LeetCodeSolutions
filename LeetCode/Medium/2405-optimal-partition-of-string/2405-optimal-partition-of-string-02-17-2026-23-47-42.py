class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        containsarr = []
        start = 0 
        end = 0
        while end < len(s):
            if s[end] not in containsarr:
                containsarr.append(s[end])
                end+=1
            else:
                start = end
                count+=1
                containsarr = []
        return count+1

        