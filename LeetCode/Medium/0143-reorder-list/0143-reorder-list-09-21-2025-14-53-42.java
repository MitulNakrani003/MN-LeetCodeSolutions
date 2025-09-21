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

    private ListNode recursiveSolution(ListNode start, ListNode endNext)
    {
        if(start == endNext)
        {
            return null;
        }
        if(start.next == endNext)
        {
            System.out.println("Value" + start.val);
            start.next = null;
            return start;
        }
        ListNode end = start;
        while(end.next != endNext)
        {
            end = end.next;
        }
        ListNode newStart = start.next;
        start.next = end;
        end.next = recursiveSolution(newStart, end);
        return start;
    }

    public void reorderList(ListNode head) {
        head = recursiveSolution(head, null);
    }
}