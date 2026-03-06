class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {}
        for i in range(1,n+1):
            graph[i] = []
        for u, v, w in times:
            graph[u].append((w,v))
        
        minheap = []
        heapq.heappush(minheap,(0,k))
        visited = set()
        mindelay = float('-inf')
        while minheap:
            nodew, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            mindelay = max(mindelay,nodew)
            for w, v in graph[node]:
                heapq.heappush(minheap,(w+nodew,v))
        if len(visited) == n:
            return mindelay
        else:
            return -1
            


        
