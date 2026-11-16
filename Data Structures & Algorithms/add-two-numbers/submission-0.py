# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Straightforward solution is O(i + j + k)
        """
        num1, num2 = [], []
        cur = l1
        while cur:
            num1.append(str(cur.val))
            cur = cur.next

        cur = l2
        while cur:
            num2.append(str(cur.val))
            cur = cur.next

        num1 = int("".join(num1[::-1]))
        num2 = int("".join(num2[::-1]))
        num3 = list(str(num1 + num2))

        dummy = ListNode()
        cur = dummy
        while num3:
            cur.next = ListNode(int(num3.pop()))
            cur = cur.next

        return dummy.next
