class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
        n = len(hand)
        freqMap = defaultdict(int)
        for x in hand:
            freqMap[x]+=1
        
        sortedkeys = sorted(freqMap.keys())
        for x in sortedkeys:
            while freqMap[x] > 0: 
                for i in range(x, x + groupSize):
                    if freqMap[i] <= 0:
                        return False
                    freqMap[i] -= 1

        return True