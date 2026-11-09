# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Two pointers approach where fast pointer is twice as fast
        as the slow pointer.

        Once fast is at the end of the LinkedList, split / treat it as two 
        LinkedList starting at the slow and fast pointer marks.

        Keep a tmp pointer at midpoint and reverse second half 
        LinkedList while iterating towards fast.

        Interweave the merging of the fast pointer LinkedList with the first ListNode, then
        the slow pointer LinkedList.

        Space: O(1) — no extra space used
        Time: O(n + m) where n is length of LinkedList and m is length of the split LinkedList.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next

            # By the time fast is at the end of the list, slow
            # would be mid point.
            fast = fast.next.next

        # Slow is at midpoint, hence slow.next is the start to the second
        # LinkedList.
        second = slow.next
        prev = slow.next = None

        # Reverse the second half LinkedList.
        while second:
            tmp = second.next
            second.next = prev
            prev = second # Holds the last second half ListNode
            second = tmp # Will be None at the tail to conclude the while loop

        # Second here is at the end of the second half LinkedList (the new head)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 # Move operation to next iteration 
