class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        visited = set()
        q = deque()

        def addValidAdjacentRooms(i,j):
            neighbours = [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]
            for x in neighbours:
                if x not in visited and x[0]>=0 and x[0]<m and x[1]>=0 and x[1]<n and rooms[x[0]][x[1]] != -1:
                    q.append(x)
                    visited.add(x)

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        distance = 0
        while q:
            for x in range(len(q)):
                i, j = q.popleft()
                rooms[i][j] = distance
                addValidAdjacentRooms(i,j)
            distance+=1
