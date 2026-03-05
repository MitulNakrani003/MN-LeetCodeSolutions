class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        aq = deque()
        pq = deque()
        pvisited = set()
        avisited = set()

        def getMeHigher(i,j):
            neighbours = [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]
            result = []
            for x in neighbours:
                if 0<=x[0]<m and 0<=x[1]<n and heights[x[0]][x[1]] >= heights[i][j]:
                    result.append(x)
            return result
            
        for j in range(n):
            pq.append((0, j))
        for i in range(m):
            pq.append((i, 0))
        for j in range(n):
            aq.append((m-1, j))
        for i in range(m):
            aq.append((i, n-1))
        
        while aq:
            mi, mj = aq.popleft()
            avisited.add((mi,mj))
            for x in getMeHigher(mi,mj):
                if x not in avisited:
                    aq.append(x)
                    avisited.add(x)
        while pq:
            mi, mj = pq.popleft()
            pvisited.add((mi,mj))
            for x in getMeHigher(mi,mj):
                if x not in pvisited:
                    pq.append(x)
                    pvisited.add(x)
        intersection_set = avisited.intersection(pvisited)
        res = []
        for item in intersection_set:
            res.append(list(item))
        return res


        
            


