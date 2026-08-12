# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if not root:
            return []
        q.append(root)
        ans=[]
    
        while q:
            s = len(q)
            temp=[]
            for _ in range(s):
                node = q.popleft()
                temp.append(node.val)
                q.append(node.left) if node.left else _
                q.append(node.right) if node.right else _
            ans.append(temp)



        return ans
