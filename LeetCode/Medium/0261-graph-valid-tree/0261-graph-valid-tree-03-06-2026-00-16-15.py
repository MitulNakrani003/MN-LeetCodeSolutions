class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            print("hello")
            return False
        graph = {}
        for i in range(n):
            graph[i] = []
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        q=deque()
        visited=set()
        q.append(0)
        while q:
            node=q.popleft()
            visited.add(node)
            for x in graph[node]:
                if x not in visited:
                    visited.add(node)
                    q.append(x)
        if len(visited)==n:
            return True
        else:
            return False