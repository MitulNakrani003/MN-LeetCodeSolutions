"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        q = deque()
        root.next = None
        q.append(root)
        while q:
            prev = None
            for i in range(len(q)):
                topnode = q.popleft()
                leftnode = topnode.left 
                rightnode = topnode.right
                if leftnode:
                    if prev != None:
                        prev.next = leftnode
                    prev = leftnode
                    q.append(leftnode)
                if rightnode:
                    if prev != None:
                        prev.next = rightnode
                    prev = rightnode
                    q.append(rightnode)
            if prev != None:
                prev.next = None
        return root

