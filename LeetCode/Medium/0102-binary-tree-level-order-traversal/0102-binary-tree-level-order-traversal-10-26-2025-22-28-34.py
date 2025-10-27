# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        levels = [[root]]
        answerlevels = [[root.val]]
        i = 0
        while True:
            thislevel = []
            vallevels = []
            for x in levels[i]:
                if x.left:
                    thislevel.append(x.left)
                    vallevels.append(x.left.val)
                if x.right:
                    thislevel.append(x.right)
                    vallevels.append(x.right.val)
            if len(thislevel) == 0:
                break
            levels.append(thislevel)
            answerlevels.append(vallevels)
            i+=1
        return answerlevels

