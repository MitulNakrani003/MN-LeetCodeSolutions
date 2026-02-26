class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        cache = {}
        def dfs(i):
            if i >= len(questions):
                return 0
            if i in cache:
                return cache[i]
            
            a = questions[i][0] + dfs(i+questions[i][1]+1)
            b = dfs(i+1)
            ret = max(a,b)
            cache[i] = ret
            return ret
        return dfs(0)
            