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
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var dummy = ListNode(0)
        var tail = dummy
        var p1 = l1
        var p2 = l2
        var carry = 0
        while(p1 != nil || p2 != nil || carry>0){
            var a = p1?.val ?? 0
            var b = p2?.val ?? 0
            var newValue = (a+b+carry)%10
            tail.next = ListNode(newValue) 
            carry = (a+b+carry)/10
            tail = tail.next!
            p1 = p1?.next
            p2 = p2?.next
        }
        return dummy.next
    }
}
