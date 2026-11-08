# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False

        # Use slow as cur, fast as a forward pointer.
        slow = fast = head

        # Fast will move twice as fast as slow pointer
        # in traversing the linked list. It will ultimately reach
        # the slow pointer, thus concluding that there's a loop.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast: return True

        return False
