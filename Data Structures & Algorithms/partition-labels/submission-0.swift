class Solution {
    func partitionLabels(_ s: String) -> [Int] {
        var mp = Dictionary<Character,Int>()
        var chars = Array(s)
        for i in 0..<s.count{
            mp[chars[i]]=i
        }
        var ans = Array<Int>()
        var start = 0
        var end = 0
        for i in 0..<s.count{
            end = max(end,mp[chars[i]]!)
            if i==end{
                ans.append(end-start+1)
                start = i+1
            }
        }
        return ans
    }
}
