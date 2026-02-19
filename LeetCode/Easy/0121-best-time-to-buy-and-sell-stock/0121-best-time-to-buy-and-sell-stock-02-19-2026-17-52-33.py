class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        currprof = 0
        i, j = 0, 0
        while j < len(prices):
            if prices[j] - prices[i] < 0:
                i = j
            else:
                currprof = prices[j] - prices[i]
            maxprof = max(currprof,maxprof)
            j+=1
        print(maxprof)
        return maxprof
