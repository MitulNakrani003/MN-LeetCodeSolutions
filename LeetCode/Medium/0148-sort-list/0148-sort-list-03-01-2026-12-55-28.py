# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getMeStartAndMiddlePointers(head):
            fast = head
            slow = head
            while fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
            prev = slow
            slow = slow.next
            prev.next = None
            return head, slow
        
        def mergeLLinConstantSpace(l1,l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2   
            return dummy.next
        
        def sortList(head):
            if head == None or head.next == None:
                return head
            
            split1, split2 = getMeStartAndMiddlePointers(head)
            print("hey")
            print(split1.val,split2.val)
            m1 = sortList(split1)
            m2 = sortList(split2)
            print(m1.val,m2.val)
            final = mergeLLinConstantSpace(m1,m2)
            return final

        return sortList(head)        