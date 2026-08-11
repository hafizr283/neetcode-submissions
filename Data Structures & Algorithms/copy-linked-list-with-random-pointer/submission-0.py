"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head
        hashmap={None:None}
        while cur:
            hashmap[cur]=Node(cur.val)
            cur=cur.next
        cur = head
        while cur:
            newnode = hashmap[cur]
            newnode.next=hashmap[cur.next]
            newnode.random=hashmap[cur.random]
            cur=cur.next
        return hashmap[head]

