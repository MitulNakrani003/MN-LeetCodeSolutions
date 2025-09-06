/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null)
        {
            return list2;
        }
        ListNode curr1 = list1;
        ListNode curr1prev = new ListNode();
        curr1prev.next = curr1;
        ListNode returnto = curr1prev;
        ListNode curr2 = list2;
        while(curr1 != null && curr2 != null)
        {
            if(curr1.val <= curr2.val)
            {
                curr1prev = curr1;
                curr1 = curr1.next;
            }
            else
            {
                curr1prev.next = curr2;
                curr2 = curr2.next;
                curr1prev = curr1prev.next;
                curr1prev.next = curr1;
            }
        }
        if(curr1 == null)
        {
            curr1prev.next = curr2;
        }
        return returnto.next;
    }
}