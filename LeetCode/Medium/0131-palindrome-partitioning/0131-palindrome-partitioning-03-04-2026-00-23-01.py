class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]
        
        result = []
        currpath = []
        def dfs(start):
            if start == len(s):
                result.append(currpath.copy())
                return
            
            for i in range(start+1,len(s)+1):
                if isPalindrome(s[start:i]):
                    currpath.append(s[start:i])
                    dfs(i)
                    currpath.pop()

        dfs(0)
        return result