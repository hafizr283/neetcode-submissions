class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        if s.count != t.count {
            return false
        }
        var ss = Array(s)
        var tt = Array(t)
        var hash1:[Character:Int]=[:]      
        var hash2:[Character:Int]=[:]
        for x in ss{
            hash1[x,default:0]+=1
        }
        for x in tt{
            hash2[x,default:0]+=1
        }
        return hash1==hash2

    }
}
