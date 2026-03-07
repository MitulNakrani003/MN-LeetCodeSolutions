class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = defaultdict(int)
        minheap = []
        for x in nums:
            freqmap[x]+=1
        for key,v in freqmap.items():
            heapq.heappush(minheap,(v,key))
        value = 0
        for i in range(len(freqmap)-k):
            heapq.heappop(minheap)
        return [x[1] for x in minheap]
