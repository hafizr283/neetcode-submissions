class Solution {
    func hammingWeight(_ n: Int) -> Int {
        var a = n
        var cnt = 0
        while a>0{
            cnt+=1
            a=(a&(a-1))
        }
        return cnt

    }
}
