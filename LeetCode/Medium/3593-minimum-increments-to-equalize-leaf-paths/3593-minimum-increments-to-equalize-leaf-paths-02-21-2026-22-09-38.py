class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        tree = defaultdict(list)
        for x in edges:
            tree[x[0]].append(x[1])
            tree[x[1]].append(x[0])

        print(tree)
        count = 0
        def dfs(node, parent):
            nonlocal count
            childmaxes = []

            for x in tree[node]:
                if x != parent:
                    childmaxes.append(dfs(x,node))
            
            if not childmaxes:
                return cost[node]
            
            maxchild = max(childmaxes)

            for x in childmaxes:
                if x < maxchild:
                    count+=1
            
            return cost[node] + maxchild

        temp = dfs(0,-1)
        return count

        