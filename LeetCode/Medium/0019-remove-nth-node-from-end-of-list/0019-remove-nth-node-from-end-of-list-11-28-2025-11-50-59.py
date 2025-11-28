# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        left = right = head
        count = 1
        while count != n:
            right = right.next
            count+=1
        while right.next != None:
            left = left.next
            right = right.next

        if left == head:
            return head.next

        prev = head
        while prev.next != left:
            prev = prev.next
        prev.next = left.next
        left.next = None
        return head