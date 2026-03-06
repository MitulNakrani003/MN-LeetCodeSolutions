class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegree = {}
        for i in range(numCourses):
            graph[i] = []
            indegree[i] = 0
        for x in prerequisites:
            graph[x[0]].append(x[1])
            indegree[x[1]]+=1
        
        q = deque()
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        path = []
        while q:
            node = q.popleft()
            path.append(node)
            for x in graph[node]:
                indegree[x]-=1
                if indegree[x] == 0:
                    q.append(x)
        print(path)
        if len(path) == len(indegree):
            return path[::-1]
        else:
            return []

