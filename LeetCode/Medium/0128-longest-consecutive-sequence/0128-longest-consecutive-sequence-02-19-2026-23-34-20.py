class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #value:index map
        if not nums:
            return 0
        # locmap = {}
        # for i, x in enumerate(nums):
        #     locmap[x] = i
        # maxlen = 1
        maxlen = 1
        numsset = set(nums)
        for x in numsset:
            if x+1 not in numsset:
                curr = x
                print(x)
                while curr-1 in numsset:
                    curr-=1
                maxlen = max(maxlen, x - curr + 1)
        return maxlen



