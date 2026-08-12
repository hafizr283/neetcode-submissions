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
    
        while True:
            l =[]
            list_for_ans=[]
            while q:
                l.append(q.popleft())
                
            if not l:
                break
            for x in l:
                list_for_ans.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            ans.append(list_for_ans)
        return ans
