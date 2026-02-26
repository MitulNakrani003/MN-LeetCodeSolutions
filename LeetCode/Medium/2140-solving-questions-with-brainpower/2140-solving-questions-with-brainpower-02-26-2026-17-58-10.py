class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        if len(questions) == 1:
            return questions[0][0]
        n = len(questions)
        dp = [0]*n
        dp[n-1] = questions[n-1][0]
        maxval = 0
        for i in range(n-2,-1,-1):
            a = dp[i+1]
            newval =  dp[i+questions[i][1]+1] if i+questions[i][1]+1 < n else 0
            b = questions[i][0] + newval
            print(i,a,b)
            dp[i] = max(a,b)    
            maxval = max(maxval,dp[i])
        return maxval        

            