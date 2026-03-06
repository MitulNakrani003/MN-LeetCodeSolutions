class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for u, v in prerequisites:
            graph[v].append(u)
        
        def isReachable(start,end):
            q = deque()
            q.append(start)
            visited = set()
            while q:
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for x in graph[node]:
                    if x == end:
                        return True
                    q.append(x)
            return False

        res = []
        for u,v in queries:
            res.append(isReachable(v,u))
        return res
