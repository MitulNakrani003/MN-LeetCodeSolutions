# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = deque()
        q.append(root)
        pathlen = 1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left == None and node.right == None:
                    return pathlen
                q.append(node.left) if node.left != None else None
                q.append(node.right) if node.right != None else None
            pathlen+=1
        return pathlen
                