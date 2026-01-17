# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        def revtotal(start, end):
            curr = start.next
            prev = start
            while prev != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return start, end
        
        zeroth = ListNode()
        zeroth.next = head
        l = zeroth
        r = head

        while True:
            flag = 0
            for _ in range(k-1):
                if r == None or r.next == None:
                    flag += 1
                    break
                r = r.next
            if flag == 1:
                break
            end = r
            r = r.next
            start = l.next
            print(start.val, end.val)
            st, ed = revtotal(start,end)
            st.next = r
            l.next = ed
            l = st

        return zeroth.next