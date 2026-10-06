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
    func reorderList(_ head: ListNode?) {
         var fast = head
         var slow = head
         while fast != nil && fast?.next != nil && fast?.next?.next != nil{
            fast = fast?.next?.next
            slow = slow?.next
        }
        var new = slow?.next
        slow?.next = nil
        var current = new
        var prev:ListNode? = nil
        while current != nil{
            var later = current?.next
            current?.next = prev 
            prev = current
            current = later
        }
        var start = head
        

        // prev + start 

        while prev != nil{
            let nextPrev = prev?.next
            let nextStart = start?.next
            start?.next = prev 
            start?.next?.next = nextStart
            prev = nextPrev
            start = nextStart
        }
       
       
        
    
    }
}
