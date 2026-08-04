# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        i1 = list1
        i2 = list2
        dummy = ListNode()
        tail = dummy
        while i1 and i2:
            if i1.val < i2.val:
                tail.next = i1
                i1 = i1.next
            else:
                tail.next = i2
                i2 = i2.next
            tail = tail.next

        if i1:
            tail.next = i1
        elif i2:
            tail.next = i2
        return dummy.next
