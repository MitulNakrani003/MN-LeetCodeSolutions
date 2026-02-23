class Solution:
    def findLHS(self, nums: List[int]) -> int:
        locmap = defaultdict(int)
        for i, x in enumerate(nums):
            locmap[x]+=1
        print(locmap)
        maxharmonious = 0
        for x in locmap.keys():
            if x-1 in locmap:
                maxharmonious = max(maxharmonious,locmap[x] + locmap[x-1])
        return maxharmonious