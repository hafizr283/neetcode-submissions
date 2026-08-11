# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode],d=0) -> int:
        if not root:
            return d;
        a=self.maxDepth(root.left,d+1)
        b=self.maxDepth(root.right,d+1)
        return max(a,b)
