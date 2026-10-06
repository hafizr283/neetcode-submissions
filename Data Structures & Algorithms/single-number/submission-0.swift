class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var ans = 0
        for x in nums{
            ans = x^ans
        }
        return ans

    }
}
