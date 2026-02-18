class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxwindowlen = 0
        maxwindow = []
        for i in range(len(s)):
            currval = s[i]
            left = i
            right = i
            prevval = s[i-1] if i-1>=0 else None
            if prevval and currval == prevval:
                left = i-1
            while left >=0 and right < len(s) and s[left] == s[right]:
                if right-left+1>maxwindowlen:
                    maxwindowlen = right-left+1
                    maxwindow = []
                    curr = left
                    while curr <= right:
                        maxwindow.append(s[curr]) 
                        curr+=1
                left-=1
                right+=1
        print(maxwindow)
        return "".join(maxwindow)
            

