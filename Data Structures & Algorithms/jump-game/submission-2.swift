class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        var valid = 0
       for i in 0..<nums.count{
        var x = i
        var y = i+nums[i]
        if(valid>=x){
            valid=max(valid,y)
        }
       }
       if(valid>=nums.count-1){
        return true
       }
       return false
    }
}
