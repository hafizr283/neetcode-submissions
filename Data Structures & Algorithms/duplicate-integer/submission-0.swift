class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        var s = Set<Int>()
        for x in nums{
            if s.contains(x){
                return true
            }
            s.insert(x)
        }
        return false
    }
}
