# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def height(root):
            if not root:
                return 0

            a = height(root.left)
            b=height(root.right)
            if abs(a-b)>1:
                self.bal=False
            return 1+max(a,b)
        height(root)
        return self.bal
