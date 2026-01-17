# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        
        countlength = 1
        curr = head
        while curr.next != None:
            curr = curr.next
            countlength += 1

        
        abslength = k%countlength

        if abslength == 0:
            return head

        golength = countlength-abslength

        end = head
        for _ in range(1,golength):
            end = end.next
        ret = end.next
        end.next = None
        curr.next = head
        return ret



        
