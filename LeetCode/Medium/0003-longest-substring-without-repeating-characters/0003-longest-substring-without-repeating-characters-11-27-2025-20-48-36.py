class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        window = []
        maxlen = 0
        left = right = 0
        while right < len(s):
            if s[right] not in window:
                window.append(s[right])
                right+=1
            else:
                while s[left] != s[right]:
                    window.remove(s[left])
                    left+=1
                window.remove(s[left])
                left+=1
            maxlen = max(maxlen,len(window))
        return maxlen
