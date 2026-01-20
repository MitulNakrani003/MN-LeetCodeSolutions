class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        cache = {}
        def dfs(i):
            if i == len(rides):
                return 0
            if i in cache:
                return cache[i]
            
            res = dfs(i+1)

            j = bisect.bisect(rides, [rides[i][1], -1, -1] )
            cache[i] = res = max(res, (rides[i][1]-rides[i][0]+rides[i][2]) + dfs(j))
            
            return res 
        return dfs(0)