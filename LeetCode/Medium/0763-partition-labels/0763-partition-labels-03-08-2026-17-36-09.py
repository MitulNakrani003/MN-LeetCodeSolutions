class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        partlengths = []
        lastIndexMap = {}
        for i in range(len(s)):
            lastIndexMap[s[i]] = i
        startindex = 0
        lastindex = 0
        partitionlengths = []
        for i in range(len(s)):
            lastindex = max(lastindex,lastIndexMap[s[i]])
            if lastindex == i:
                partitionlengths.append(lastindex-startindex+1)
                startindex = lastindex+1
            
        return partitionlengths
            

               





        
