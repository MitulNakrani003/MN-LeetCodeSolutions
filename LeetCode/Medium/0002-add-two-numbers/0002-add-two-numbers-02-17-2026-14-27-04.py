# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2
        carry = 0
        returnHead = ListNode()
        returnCurrent = returnHead
        while pointer1 != None and pointer2 != None:
            totalsum = pointer1.val + pointer2.val + carry
            remval = totalsum % 10
            carry = totalsum // 10
            returnCurrent.next = ListNode(remval)
            returnCurrent = returnCurrent.next
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        if pointer1 != None:
            while pointer1 != None:
                totalsum = pointer1.val + carry
                remval = totalsum % 10
                carry = totalsum // 10
                returnCurrent.next = ListNode(remval)
                returnCurrent = returnCurrent.next
                pointer1 = pointer1.next
        if pointer2 != None:
            while pointer2 != None:
                totalsum = pointer2.val + carry
                remval = totalsum % 10
                carry = totalsum // 10
                returnCurrent.next = ListNode(remval)
                returnCurrent = returnCurrent.next
                pointer2 = pointer2.next
        if carry > 0:
            returnCurrent.next = ListNode(carry)
            returnCurrent = returnCurrent.next
        return returnHead.next

        
