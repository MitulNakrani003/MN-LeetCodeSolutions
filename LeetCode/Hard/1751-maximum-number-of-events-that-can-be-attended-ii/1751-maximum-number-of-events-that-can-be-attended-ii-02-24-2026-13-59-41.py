class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        cache = {}
        def dfs(index, remaining):
            if index == len(events) or remaining == 0:
                return 0
            if (index,remaining) in cache:
                return cache[(index,remaining)]

            a = dfs(index+1, remaining)
            newindex = bisect.bisect_right(events,[events[index][1],float('inf'),float('inf')])
            b = events[index][2] + dfs(newindex, remaining-1)
            res = max(a,b)
            cache[(index,remaining)] = res
            return res
        return dfs(0, k)
