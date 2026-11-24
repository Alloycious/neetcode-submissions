# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Nodes are considered "good" if paths from root node
        to node x have values greater than node x.

        DFS to traverse nodes and keep track of whether a path is good or not.

        A node is good only when node.val >= max val of the nodes preceding int
        from the root. Traverse the tree via pre-order and compute if current 
        node is good before going onto the next nodes.
        """
        def dfs(node: Optional[TreeNode], max_val: int):
            if node is None:
                return 0

            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res

        return dfs(root, root.val)
