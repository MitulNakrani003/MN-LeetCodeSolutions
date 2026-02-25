class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}
        def dfs(index,robberyamount):
            if index >= len(nums):
                return robberyamount
            if (index,robberyamount) in cache:
                return cache[(index,robberyamount)]
            a = dfs(index+1,robberyamount)
            b = dfs(index+2,robberyamount+nums[index])

            res = max(a,b)
            cache[(index,robberyamount)] = res
            return res
        return dfs(0,0)