# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans =0
        def dfs(root,max_number=root.val):
            nonlocal ans
            if not root:
                return;
            if root.val>=max_number:
                ans=ans+1

            max_number=max(max_number,root.val)
            dfs(root.left,max_number)
            dfs(root.right,max_number)
        dfs(root)
        return ans

           