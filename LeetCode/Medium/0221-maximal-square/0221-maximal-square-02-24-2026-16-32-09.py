class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for x in range(m)]

        maxnum = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                left = dp[i][j-1] if j>0 else 0
                top = dp[i-1][j] if i>0 else 0
                diagonal = dp[i-1][j-1] if (i>0 and j>0) else 0
                dp[i][j] = min([int(left),int(top),int(diagonal)])+1
        
                maxnum = max(maxnum,dp[i][j])
        print(dp)
        if maxnum == -1:
            return 0
        return maxnum ** 2
