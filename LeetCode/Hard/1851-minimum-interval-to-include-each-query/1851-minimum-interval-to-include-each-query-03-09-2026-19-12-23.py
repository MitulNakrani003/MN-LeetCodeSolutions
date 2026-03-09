class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        idx = 0
        result = {}
        minheap = []
        original_queries = queries[:]
        queries.sort()
        for i in range(len(queries)):
            while idx < len(intervals) and intervals[idx][0] <= queries[i]:
                heapq.heappush(minheap,(intervals[idx][1]-intervals[idx][0]+1,intervals[idx][1]))
                idx+=1
            while minheap and minheap[0][1] < queries[i]:
                heapq.heappop(minheap)
            
            if minheap:
                result[queries[i]] = (minheap[0][0])
            else:
                result[queries[i]] = -1
        finalresult = []
        for i in original_queries:
            finalresult.append(result[i])
        return finalresult
        
