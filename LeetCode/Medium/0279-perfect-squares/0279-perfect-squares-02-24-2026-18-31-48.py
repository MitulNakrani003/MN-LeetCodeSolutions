class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [n for x in range(n+1)]
        dp[0] = 0
        print(dp)
        for target in range(1,n+1):
            for s in range(1,target+1):
                sqval = s ** 2
                if (target - sqval) < 0:
                    break
                dp[target] = min(dp[target], 1+dp[target-sqval])

        return dp[n]

                
            
