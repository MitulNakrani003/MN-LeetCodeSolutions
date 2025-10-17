# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self,tree1,tree2):
        if(tree1 == None and tree2 == None):
            return True
        if((tree1 == None and tree2 != None) or (tree1 != None and tree2 == None)):
            return False
        if(tree1.val == tree2.val and self.isSameTree(tree1.left,tree2.left) and self.isSameTree(tree1.right,tree2.right)):
            return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root == None):
            return False
        if(root.val == subRoot.val):
            if(self.isSameTree(root,subRoot)):
                return True
        
        if(self.isSubtree(root.left,subRoot)):
            return True
        elif(self.isSubtree(root.right,subRoot)):
            return True
        else:
            return False
        