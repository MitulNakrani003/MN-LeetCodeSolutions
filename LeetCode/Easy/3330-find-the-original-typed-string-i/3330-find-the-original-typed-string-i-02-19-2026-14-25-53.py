class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        previous = ""
        i = 0
        while i < len(word):
            if previous == word[i]:
                curr = i
                while curr < len(word) and word[curr] == word[curr-1]:
                    count+=1
                    curr+=1
                i = curr
                previous = word[i-1]
            else:
                previous = word[i]
                i+=1
        print(count)
        return count
            

