class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        freshoranges = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshoranges+=1
                if grid[i][j] == 2:
                    q.append((i,j))
        if freshoranges == 0:
            return 0

        def getOrangeNeighbours(i,j):
            neighbours = [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]
            result = []
            for x in neighbours:
                if x[0] >= 0 and x[0] < m and x[1] >= 0 and x[1] < n and grid[x[0]][x[1]] == 1 and x not in visited:
                    result.append(x)
            return result
        
        minutes = -1
        while q:
            for i in range(len(q)):
                oi, oj = q.popleft()
                visited.add((oi,oj))
                for x in getOrangeNeighbours(oi,oj):
                    visited.add(x)
                    freshoranges -=1
                    q.append(x)
            minutes+=1
        
        if freshoranges == 0:
            return minutes
        else:
            return -1

