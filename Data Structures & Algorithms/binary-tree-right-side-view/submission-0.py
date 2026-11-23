# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Since we want nodes visible from the right side of the tree, 
        visible nodes are guaranteed to be the right most side of the tree.

        We can get those nodes by performing post-order traversal DFS on the right nodes first.
        Subsequently, we also keep track of left-side nodes which depths are further than 
        the right most node's leaf.

        Notes: Post-order traversal -> right -> left -> root
        """
        if root is None: return []
        res = []

        def dfs(node: Optional[TreeNode], depth: int):
            if node is None:
                return

            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res
