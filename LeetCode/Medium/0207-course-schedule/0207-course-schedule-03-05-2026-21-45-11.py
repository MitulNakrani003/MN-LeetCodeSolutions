class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        graph = defaultdict(list)
        indegree = {}
        for x in prerequisites:
            graph[x[0]].append(x[1])
            if x[0] not in indegree:
                indegree[x[0]] = 0
            if x[1] not in indegree:
                indegree[x[1]] = 0
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
            return True
        else:
            return False



        
        
        
        
