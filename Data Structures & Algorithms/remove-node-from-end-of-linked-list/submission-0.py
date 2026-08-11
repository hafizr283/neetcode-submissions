# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L=head
        R=head
        for _ in range(n):
            R=R.next
        if not R: 
            return head.next
        prev = L
        while R:
            prev=L
            L=L.next
            R=R.next
        prev.next=L.next
        return head
