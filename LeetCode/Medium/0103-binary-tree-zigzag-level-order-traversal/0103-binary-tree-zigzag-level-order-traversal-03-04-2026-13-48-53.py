# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = deque()
        q.append(root)
        res = []
        direction = 1
        while q:
            curr = []
            for i in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                q.append(node.right) if node.right != None else None
                q.append(node.left) if node.left != None else None
            if direction == 1:
                curr = curr[::-1]
            direction *= (-1) 
            res.append(curr)
        print(res)
        return res
                



