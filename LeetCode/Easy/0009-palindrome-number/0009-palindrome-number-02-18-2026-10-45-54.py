class Solution:
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)
        end = len(strnum)-1
        start = 0
        while start <= end:
            if strnum[start] != strnum[end]:
                return False
            else:
                start+=1
                end-=1
        return True

                

            