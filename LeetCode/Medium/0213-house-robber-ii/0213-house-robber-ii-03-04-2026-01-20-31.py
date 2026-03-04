class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(arr):
            if not arr:
                return 0
            print(arr)
            prev2value = 0
            prevvalue = arr[0]
            for i in range(1,len(arr)):
                take = arr[i] + prev2value
                nottake = prevvalue
                curr = max(take, nottake)
                prev2value = prevvalue
                prevvalue = curr
            return prevvalue
        
        return max([dfs(nums[:-1]),dfs(nums[1:]),dfs([nums[0]])])
    