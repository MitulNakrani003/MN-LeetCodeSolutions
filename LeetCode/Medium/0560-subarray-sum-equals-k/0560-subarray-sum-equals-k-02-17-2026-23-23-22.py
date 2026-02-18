class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixsum = 0
        prefixmap = {0:1}
        for x in nums:
            prefixsum+=x
            if prefixsum-k in prefixmap:
                count+=prefixmap[prefixsum-k]
            prefixmap[prefixsum] = prefixmap.get(prefixsum,0)+1
        return count
            
