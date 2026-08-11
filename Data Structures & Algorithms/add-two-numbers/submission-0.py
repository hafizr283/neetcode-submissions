# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans = dummy
        carry=0
        while l1 or l2 or carry:
            a,b=0,0
            if l1:
                a = l1.val
                l1=l1.next
            if l2:
                b=l2.val
                l2=l2.next
            a= a+b+carry
            carry=a//10
            ans.next=ListNode(a%10)
            ans=ans.next
        ans=None
        return dummy.next
