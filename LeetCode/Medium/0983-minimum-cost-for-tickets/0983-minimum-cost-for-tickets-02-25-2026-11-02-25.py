class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        oneday = costs[0]
        sevenday = costs[1]
        thirtyday = costs[2]
        
        cache = {}
        def dfs(i):
            if i >= len(days):
                return 0
            if i in cache:
                return cache[i]

            a = dfs(i+1) + oneday
            plus7day = days[i] + 7 - 1
            j = bisect.bisect_right(days,plus7day)
            b = dfs(j) + sevenday
            plus30day = days[i] + 30 - 1
            k = bisect.bisect_right(days,plus30day)
            c = dfs(k) + thirtyday
            res = min(a,b,c)
            cache[i] = res
            return res
        return dfs(0)

            
