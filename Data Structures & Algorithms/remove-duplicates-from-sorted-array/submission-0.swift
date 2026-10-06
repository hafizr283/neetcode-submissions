class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        if nums.count == 0{
            return 0
        }
        var w = 0
        for r in 0..<nums.count{
            if nums[w] != nums[r]{
                nums[w+1]=nums[r]
                w+=1
            }
        }
        return w+1
    }
}
