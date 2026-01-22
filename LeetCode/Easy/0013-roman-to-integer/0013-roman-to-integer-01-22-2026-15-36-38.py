class Solution:
    def romanToInt(self, s: str) -> int:
        finalsum = 0
        i = 0
        valuemap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while i < (len(s)):
            if s[i] == 'I':
                if i+1 >= len(s):
                    finalsum+=valuemap[s[i]]
                    i+=1
                    continue
                next = s[i+1]
                if next == 'V' or next == 'X':
                    finalsum+=(valuemap[next]-valuemap[s[i]])
                    i += 2
                else:
                    finalsum+=valuemap[s[i]]
                    i+=1
            elif s[i] == 'X':
                if i+1 >= len(s):
                    finalsum+=valuemap[s[i]]
                    i+=1
                    continue
                next = s[i+1]
                if next == 'L' or next == 'C':
                    finalsum+=(valuemap[next]-valuemap[s[i]])
                    i += 2
                else:
                    finalsum+=valuemap[s[i]]
                    i+=1
            elif s[i] == 'C':
                if i+1 >= len(s):
                    finalsum+=valuemap[s[i]]
                    i+=1
                    continue
                next = s[i+1]
                if next == 'D' or next == 'M':
                    finalsum+=(valuemap[next]-valuemap[s[i]])
                    i += 2
                else:
                    finalsum+=valuemap[s[i]]
                    i+=1
            else:
                finalsum+=valuemap[s[i]]
                i+=1


        return finalsum