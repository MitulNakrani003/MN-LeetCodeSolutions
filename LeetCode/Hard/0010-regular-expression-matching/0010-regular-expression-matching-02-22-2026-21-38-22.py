class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= len(s) and j >= len(p):
                result = True
            elif i >= len(s):
                if (j+1) < len(p) and p[j+1] == '*':
                    result = dfs(i, j+2)
                else:
                    result = False
            elif i < len(s) and j >= len(p):
                result = False
            elif s[i] == p[j] or p[j] == '.':
                if (j+1) < len(p) and p[j+1] == '*':
                    result = dfs(i+1, j) or dfs(i, j+2)
                else:
                    result = dfs(i+1, j+1)
            else:
                if (j+1) < len(p) and p[j+1] == '*':
                    result = dfs(i, j+2)
                else:
                    result = False

            memo[(i, j)] = result
            return result

        return dfs(0, 0)