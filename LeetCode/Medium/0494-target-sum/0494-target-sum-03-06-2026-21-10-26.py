class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def dfs(i,total):
            if i == len(nums) and total == target:
                return 1
            if i == len(nums):
                return 0
            if (i,total) in cache:
                return cache[(i,total)]
            ways = dfs(i+1,total+nums[i]) + dfs(i+1,total-nums[i])
            cache[(i,total)] = ways
            return ways
        return dfs(0,0)


            

