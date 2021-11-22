"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = {}
        while p:
            parents[p.val] = p.parent
            p = p.parent

        while q.val not in parents:
            q = q.parent
        return q