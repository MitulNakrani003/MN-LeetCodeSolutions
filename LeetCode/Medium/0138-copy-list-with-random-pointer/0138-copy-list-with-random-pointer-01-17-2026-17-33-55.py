"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        copydict = {}
        curr = head
        prev = ListNode()
        while curr != None:
            newcurr = ListNode(curr.val)
            prev.next = newcurr
            prev = newcurr
            copydict[curr] = newcurr
            curr = curr.next

        start = head
        while start != None:
            if start.random == None:
                copydict[start].random = None
            else:
                copydict[start].random = copydict[start.random]
            start = start.next
        
        return copydict[head]
        