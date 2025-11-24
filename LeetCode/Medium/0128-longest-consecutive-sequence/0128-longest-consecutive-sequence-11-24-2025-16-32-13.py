class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for i, x in enumerate(nums):
            freq[x]=i
        
        maxlength = 0
        for i, x in enumerate(nums):
            if x-1 in freq:
                continue
            else:
                start = x + 1 
                count = 1 
                while start in freq:
                    count+=1
                    del freq[start]
                    start+=1
                    
                maxlength = max(count,maxlength)
        return maxlength
