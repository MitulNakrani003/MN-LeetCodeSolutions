class Solution:
    def climbStairs(self, n: int) -> int:
        #1D DP ARRAY
        ways = [0]*((n+1) if n > 2 else 3)
        print(ways)
        ways[1] = 1
        ways[2] = 2
        for i in range(3,n+1):
            ways[i] = ways[i-2] + ways[i-1]
        print(ways)
        
        return ways[n]
            
            