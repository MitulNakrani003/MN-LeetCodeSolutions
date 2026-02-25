class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for x in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        print(dp)
        for i in range(2,len(cost)):
            print(i)
            dp[i] = min(cost[i]+dp[i-1], cost[i]+dp[i-2])
        return min(dp[-1],dp[-2])