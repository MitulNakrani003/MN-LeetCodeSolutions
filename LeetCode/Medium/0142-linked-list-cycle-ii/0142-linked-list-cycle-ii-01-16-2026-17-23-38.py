# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        fast = head
        slow = head
        while True:
            if fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    break
            else:
                return None
        
       
        curr = head
        while True:
            if curr == fast:
                return curr
            curr = curr.next
            fast = fast.next

        