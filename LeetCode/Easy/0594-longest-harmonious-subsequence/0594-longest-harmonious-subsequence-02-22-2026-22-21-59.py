class Solution:
    def findLHS(self, nums: List[int]) -> int:
        locmap = defaultdict(list)
        for i, x in enumerate(nums):
            locmap[x].append(i)
        print(locmap)
        maxharmonious = 0
        for x in locmap.keys():
            if x-1 in locmap:
                currlen = len(locmap[x]) + len(locmap[x-1])
                print(currlen,x, x-1)
                print("--")
                maxharmonious = max(maxharmonious,currlen)
        return maxharmonious