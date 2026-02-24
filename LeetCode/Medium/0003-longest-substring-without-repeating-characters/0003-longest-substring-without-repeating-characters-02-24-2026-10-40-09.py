class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vals = set()
        i = 0
        maxlen = 0
        for j in range(len(s)):
            if s[j] in vals:
                while s[i] != s[j]:
                    vals.remove(s[i])
                    i+=1
                vals.remove(s[i])
                i+=1
                vals.add(s[j])
            else:
                vals.add(s[j])
            maxlen = max(maxlen,j-i+1)
        return maxlen
