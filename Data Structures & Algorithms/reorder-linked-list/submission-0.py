# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            print(f'slow {slow.val}')
            
        #reversing
        
        second_list = slow.next
        slow.next=None
        prev=None
        curr = second_list
        while curr:
            temp_curr=curr.next
            curr.next=prev
            prev=curr
            curr=temp_curr
        #reverse head ekhon prev
        first=head
        second = prev        
        
        
        while first and second:
            temp_first=first.next
            temp_second=second.next
            second.next=first.next
            first.next=second
            first=temp_first
            second=temp_second
        