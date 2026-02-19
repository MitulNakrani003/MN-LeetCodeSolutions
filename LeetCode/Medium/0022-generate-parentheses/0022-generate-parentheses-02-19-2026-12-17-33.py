class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #backtracking and dynamix programming
        
        result= []
        def dfs(openbrac,closedbrac,currstr):
            if openbrac == closedbrac == n:
                result.append(''.join(currstr))
                return
            
            if openbrac < n:
                # newstr = currstr.copy()
                # newstr.append("(")
                # dfs(openbrac+1,closedbrac,newstr)
                currstr.append("(")
                dfs(openbrac+1,closedbrac,currstr)
                currstr.pop()

            if openbrac-closedbrac > 0:
                # newstr2 = currstr.copy()
                # newstr2.append(")")
                # dfs(openbrac,closedbrac+1,newstr2)
                currstr.append(")")
                dfs(openbrac,closedbrac+1,currstr)
                currstr.pop()
        
        dfs(0,0,[])
        print(result)
        return result