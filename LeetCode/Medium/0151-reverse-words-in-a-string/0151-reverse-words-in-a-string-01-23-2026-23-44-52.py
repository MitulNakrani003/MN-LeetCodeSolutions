class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(" ")
        x = [i for i in x if i != '']
        x = x[::-1]
        return " ".join(x)