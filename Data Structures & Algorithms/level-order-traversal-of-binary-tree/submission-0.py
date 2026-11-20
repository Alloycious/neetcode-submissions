# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        from collections import deque
        q = deque()
        q.append(root)

        res = [[root.val]]

        while q:
            level = []
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if node.left is not None:
                    level.append(node.left.val)
                    q.append(node.left)
                    
                if node.right is not None:
                    level.append(node.right.val)
                    q.append(node.right)

            res.append(level)
        
        res.pop()
        return res
        