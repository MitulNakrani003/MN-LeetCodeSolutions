class Solution:
    def kthCharacter(self, k: int) -> str:
        previous = []
        current = ['a']
        while len(current) < k:
            righthalfstartindex = len(current)//2
            nextvalsofcurr =  []
            for i in range(righthalfstartindex,len(current)):
                nextvalsofcurr.append(chr(ord(current[i])+1))
            toappend = []
            toappend+=previous
            toappend+=nextvalsofcurr
            current+=toappend
            previous = toappend
        resultstr = "".join(current)
        return current[k-1]