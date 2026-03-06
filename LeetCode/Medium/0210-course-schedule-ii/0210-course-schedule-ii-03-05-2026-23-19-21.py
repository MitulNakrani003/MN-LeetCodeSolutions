class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for x in prerequisites:
            graph[x[0]].append(x[1])
        
        output = []
        visited = set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            for x in graph[node]:
                if dfs(x) == False:
                    return False
            cycle.remove(node)
            visited.add(node)
            output.append(node)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output



