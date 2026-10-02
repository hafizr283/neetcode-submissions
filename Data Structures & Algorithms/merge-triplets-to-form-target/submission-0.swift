class Solution {
    func mergeTriplets(_ triplets: [[Int]], _ target: [Int]) -> Bool {
        var fa = false
        var fb = false
        var fc = false

        for t in triplets{
            var x = t[0]
            var y = t[1]
            var z = t[2]
            var a = target[0]
            var b = target[1]
            var c = target[2]
            if(x>a || y>b || z>c){
                continue
            }
            if(x==a){
                fa=true
            }
            if(y==b){
                fb=true
            }
            if(z==c){
                fc=true
            }

        }
        return fa && fb && fc
    }
}
