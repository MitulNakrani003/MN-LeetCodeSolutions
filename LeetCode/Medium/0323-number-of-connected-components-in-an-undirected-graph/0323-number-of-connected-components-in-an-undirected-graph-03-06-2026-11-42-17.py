class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        components = 0
        for i in range(n):
            if i in visited:
                continue
            q = deque()
            q.append(i)
            components+=1
            while q:
                node = q.popleft()
                visited.add(node)
                for x in graph[node]:
                    if x not in visited:
                        visited.add(x)
                        q.append(x)

        return components

