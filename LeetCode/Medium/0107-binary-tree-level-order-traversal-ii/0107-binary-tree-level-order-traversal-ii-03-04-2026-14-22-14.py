# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            curr = []
            for i in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                q.append(node.left) if node.left != None else None
                q.append(node.right) if node.right != None else None
            res.append(curr)
        return res[::-1]
