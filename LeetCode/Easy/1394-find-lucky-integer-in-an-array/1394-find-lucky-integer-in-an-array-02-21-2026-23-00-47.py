class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqMap = defaultdict(int)
        for x in arr:
            freqMap[x]+=1
        maxnumber = 0
        for key, value in freqMap.items():
            if key == value:
                maxnumber = max(maxnumber,key)
        if not maxnumber:
            return -1
        return maxnumber
