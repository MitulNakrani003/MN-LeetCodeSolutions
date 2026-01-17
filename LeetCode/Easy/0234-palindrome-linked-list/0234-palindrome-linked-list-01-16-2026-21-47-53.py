# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = []
        while head != None:
            x.append(head.val)
            head = head.next
        
        start = 0
        end = len(x)-1
        while start <= end:
            if x[start] != x[end]:
                return False
            start+=1
            end-=1
        return True