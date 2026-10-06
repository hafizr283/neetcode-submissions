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
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        var dummy = ListNode(0)
        var tail = dummy
        var l1 = list1
        var l2 = list2
        while let node1=l1, let node2=l2{
            if(node1.val<=node2.val){
                tail.next = node1
                l1=node1.next

            }
            else{
                tail.next=node2
                l2=node2.next

            
            }
            tail = tail.next!
        }
        while let node1=l1{
            tail.next=node1
            l1=node1.next
            tail=tail.next!
        }
        while let node2=l2{
            tail.next=node2
            l2=node2.next
            tail=tail.next!
        }
        return dummy.next

    }
}
