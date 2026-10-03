class Solution {
    func checkValidString(_ s: String) -> Bool {
        var mx = 0
        var mn = 0
        var t = Array(s)
        for x in t{
            if x=="*"{
                mn-=1
                mx+=1
            }
            if x=="("{
                mn+=1
                mx+=1
            }
            if(x==")"){
                mn-=1
                mx-=1
            }
            if mx<0{
                return false
            }
            if mn<0{
                mn=0
            }
        }
        return mn==0

    }
}
