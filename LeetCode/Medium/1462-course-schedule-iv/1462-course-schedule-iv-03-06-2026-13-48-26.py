class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for u, v in prerequisites:
            graph[v].append(u)
        
        reachable = {}
        for start in range(numCourses):
            q = deque()
            q.append(start)
            visited = set()
            while q:
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for x in graph[node]:
                    q.append(x)
            reachable[start] = visited

        # Answer each query in O(1)
        res = []
        for u, v in queries:
            res.append(u in reachable[v])
        return res