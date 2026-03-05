class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = set()
        q = deque()

        for i in range(m):
            if board[i][0] == "O":
                q.append((i,0))
            if board[i][n-1] == "O":
                q.append((i,n-1))
        for j in range(n):
            if board[0][j] == "O":
                q.append((0,j))
            if board[m-1][j] == "O":
                q.append((m-1,j))

        print(q)
        def getNeighbours(i,j):
            neighbour = [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]
            result = []
            for x in neighbour:
                if x[0]>=0 and x[1] >=0 and x[0] < m and x[1] < n and board[x[0]][x[1]] != "X" and (x[0],x[1]) not in visited:
                    result.append(x)
            return result
        
        while q:
            nodei, nodej = q.popleft()
            board[nodei][nodej] = "#"
            for x in getNeighbours(nodei,nodej):
                q.append((x[0],x[1]))
                board[x[0]][x[1]] = "#"
                visited.add((x[0],x[1]))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"



                
                
                
