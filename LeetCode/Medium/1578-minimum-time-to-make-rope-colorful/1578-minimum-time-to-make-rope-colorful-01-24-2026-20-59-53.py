class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        if n == 1:
            return 0
        
        l = 0
        r = 1
        total = 0
        while l < n-1:
            if colors[r] != colors[l]:
                r+=1
                l+=1
            else:
                while r < n and colors[r] == colors[r-1]:
                    r+=1
                shortarr = neededTime[l:r]
                total += (sum(shortarr) - max(shortarr))
                l = r-1
        return total







