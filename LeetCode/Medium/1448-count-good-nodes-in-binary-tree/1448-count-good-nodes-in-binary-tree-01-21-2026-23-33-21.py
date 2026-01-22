# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        visited = set()
        count = 0
        def dfs(node,maxtillnowpath):
            nonlocal count
            if node == None:
                return
            if node not in visited:
                visited.add(node)
                if maxtillnowpath <= node.val:
                    count +=1
                    maxtillnowpath = max(maxtillnowpath,node.val)
                dfs(node.left,maxtillnowpath)
                dfs(node.right,maxtillnowpath)
        dfs(root,root.val)
        return count

