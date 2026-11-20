# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(left, node, right):
            if node is None:
                return True

            # Guard against invalid binary search tree
            if not (left < node.val < right):
                return False

            # Recursively interate in a DFS manner where left is the lower limit and
            # right is the upper limit value.
            return valid(left, node.left, node.val) \
                and valid(node.val, node.right, right)
        
        return valid(float("-inf"), root, float("inf"))
