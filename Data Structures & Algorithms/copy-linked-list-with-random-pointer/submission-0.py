"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Iterate twice through the LinkedList.

        First iteration memorizes the random to the h_map, second
        iteration distributes them out.

        We need the map memorization as we can't deep copy on the first pass
        since the random nodes are still not filled yet.
        """

        # key = node
        # val = random
        h_map = {None: None}
        cur = head

        # First pass: deep copy node and store cur node as key to h_map.
        # We need a key that persist between the two loops, hence we using cur node.
        while cur:
            copy = Node(cur.val)
            h_map[cur] = copy
            cur = cur.next

        # Restart the iteration at head and distribute next + random mappings.
        cur = head
        while cur:
            copy = h_map[cur]
            copy.next = h_map[cur.next]
            copy.random = h_map[cur.random]
            cur = cur.next

        return h_map[head]
