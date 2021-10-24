from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)
            return max(lh, rh) + 1

        return dfs(root)
