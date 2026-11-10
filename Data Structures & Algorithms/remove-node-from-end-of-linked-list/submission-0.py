# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two pointers approach where we move the fast pointer n steps ahead towards the
        end of the LinkedList first.

        This gap of n size guarantees that slow will reach right before the node to delete.
        From here, iterate both pointers till the end of the LinkedList, then remove nth node
        from end.
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        for _ in range(n):
            fast = fast.next

        while fast:
           slow = slow.next
           fast = fast.next 

        # Remove Nth node from end of list
        slow.next = slow.next.next

        return dummy.next
        