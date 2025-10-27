# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            arr.append(root.val)
            traversal(root.right)
        traversal(root)
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True


