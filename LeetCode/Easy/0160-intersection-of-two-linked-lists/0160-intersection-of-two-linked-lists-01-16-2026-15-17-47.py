# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB
        h1swap = 0
        h2swap = 0
        while True:
            if headA == headB:
                return headA
            
            if headA == None:
                if h1swap == 1:
                    break
                h1swap +=1
                headA = l2
            if headB == None:
                if h2swap == 1:
                    break
                h2swap += 1
                headB = l1
            
            print(headA.val, headB.val)

            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None