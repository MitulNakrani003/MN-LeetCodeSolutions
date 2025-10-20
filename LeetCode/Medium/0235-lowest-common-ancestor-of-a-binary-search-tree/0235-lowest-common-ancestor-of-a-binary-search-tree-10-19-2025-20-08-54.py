# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getPath(self, start, end):
        visited = set()
        mypath = []
        def dfs(node, path):
            if node == None:
                return None
            if node == end:
                path.append(node)
                return path
            if node.val not in visited:
                visited.add(node)
                for adjnode in [node.left,node.right]:
                    result = dfs(adjnode, path + [node])
                    if result:
                        return result
            return None
        return dfs(start, mypath)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = self.getPath(root,p)
        path2 = self.getPath(root,q)
        path1new = [x.val for x in path1]
        path2new = [x.val for x in path2]
        print(path1new)
        print(path2new)
        last = 0
        for i in range(min(len(path1),len(path2))):
            if path1[i] != path2[i]:
                return path1[i-1]
        if len(path1) <= len(path2):
            return path1[-1]
        return path2[-1]