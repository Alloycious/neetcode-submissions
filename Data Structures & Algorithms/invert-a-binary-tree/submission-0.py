# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Swap the left with the right node
        temp = left
        root.left = right
        root.right = temp
        
        return root