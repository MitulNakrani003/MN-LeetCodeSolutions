class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        count = 0
        for x in nums:
            if x == 1:
                count+=1
            if x == 0:
                count = 0
            maxcount = max(maxcount,count)
        return maxcount