# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Similar to max depth but we need to check the max depth
        of the left and right subtree of the root. 

        Traversal will be post-order: left -> right -> root.
        """
        max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter

            if node is None:
                return 0
            
            # DFS traversal
            left, right = dfs(node.left), dfs(node.right)

            # Calculated starting from the leaf nodes (depth first)
            max_diameter = max(max_diameter, left + right)

            # Return max depth
            return 1 + max(left, right)

        dfs(root)
        return max_diameter
