class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap = defaultdict(int)
        for x in s:
            freqMap[x]+=1
        for x in t:
            freqMap[x]-=1
        for x in freqMap.values():
            if x != 0:
                return False
        return True