class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqMap = {}
        for x in words:
            freqMap[x] = freqMap.get(x, 0) + 1

        # (-freq, word): min heap on -freq gives max freq first
        # word as tiebreaker gives alphabetical order for free
        heap = [(-freq, word) for word, freq in freqMap.items()]
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result