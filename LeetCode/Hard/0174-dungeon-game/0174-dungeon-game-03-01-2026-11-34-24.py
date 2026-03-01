class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        if m==1 and n==1:
            if dungeon[0][0] > 0:
                return 1
            else:
                abs(dungeon[0][0])+1
        dp = [[0]*n for x in range(m)]
        dp[m-1][n-1] = (dungeon[m-1][n-1])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    dp[i][j] = min(0,dungeon[i][j])
                elif i == m-1:
                    dp[i][j] = min(0,dungeon[i][j]+dp[i][j+1])
                elif j == n-1:
                    dp[i][j] = min(0,dungeon[i][j]+dp[i+1][j])
                else:
                    dp[i][j] = min(0,dungeon[i][j] + max(dp[i][j+1],dp[i+1][j]))
        print(dp)
        return abs(dp[0][0])+1

