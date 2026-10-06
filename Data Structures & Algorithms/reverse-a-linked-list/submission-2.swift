/**
 * Definition for singly-linked list.
 * class ListNode {
 *     var val: Int
 *     var next: ListNode?
 *     init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        var curr = head
        var prev:ListNode? = nil
        while let node = curr{
            var next = node.next
            node.next = prev 
            prev = node 
            curr = next
        }
        return prev
    }
}
