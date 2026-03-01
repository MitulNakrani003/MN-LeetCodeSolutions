class Solution:
    def minWindow(self, s: str, t: str) -> str:
        haveMap = {}
        needMap = {}
        for x in t:
            haveMap[x] = 0
            if x not in needMap:
                needMap[x] = 0
            needMap[x]+=1

        def CheckConditionFulfilled():
            if sum(haveMap.values()) < sum(needMap.values()):
                return False
            for x in needMap:
                if haveMap[x]>=needMap[x]:
                    continue
                else:
                    return False
            return True
        
        left, right = 0, 0
        minleft, minright = -1, -1
        minlen = float('inf')
        
        def UpdateMins():
            nonlocal minlen, minleft, minright
            if right-left+1 < minlen:
                minlen = right-left+1
                minleft = left
                minright = right

        while right < len(s):
            if s[right] in haveMap:             # add FIRST
                haveMap[s[right]] += 1
            while CheckConditionFulfilled():    # then check
                UpdateMins()
                if s[left] in haveMap:
                    haveMap[s[left]] -= 1
                left += 1
            right += 1

        if minleft == -1:
            return ""
        return s[minleft:minright + 1]

        

        

        


                
