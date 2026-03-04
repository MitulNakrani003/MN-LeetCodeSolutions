# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        q = deque()
        q.append((root,root.val))
        while q:
            for i in range(len(q)):
                node, value = q.popleft()
                if node.left == None and node.right == None and value == targetSum:
                    return True
                q.append((node.left,node.left.val+value)) if node.left != None else None
                q.append((node.right,node.right.val+value)) if node.right != None else None
        return False