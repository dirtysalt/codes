import java.util.*;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
    }
}

class PQItem implements Comparable<PQItem> {
    public int value;
    public ListNode node;

    public PQItem(int value, ListNode node) {
        this.value = value;
        this.node = node;
    }
    public int compareTo(PQItem x) {
        if (value < x.value) {
            return -1;
        } else if (value > x.value) {
            return 1;
        }
        return 0;
    }
}
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<PQItem> pq = new PriorityQueue<>();
        for (ListNode node : lists) {
            if (node == null) {
                continue;
            }
            pq.add(new PQItem(node.val, node));
        }
        ListNode head = new ListNode(0);
        ListNode tail = head;
        while (pq.size() != 0) {
            PQItem item = pq.poll();
            ListNode node = item.node;
            tail.next = node;
            tail = node;
            node = node.next;
            if (node != null) {
                pq.add(new PQItem(node.val, node));
            }
        }
        tail.next = null;
        head = head.next;
        return head;
    }
}