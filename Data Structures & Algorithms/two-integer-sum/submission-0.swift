class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var hash : [Int:Int] = [:]
        for (i,x) in nums.enumerated(){
            if let y=hash[target-x]{
                return [y,i]
            }
            hash[x]=i
        }
        // return false
        return []
    }
}
