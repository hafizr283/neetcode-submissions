class Solution {
    func canCompleteCircuit(_ gas: [Int], _ cost: [Int]) -> Int {

        if gas.reduce(0,+)<cost.reduce(0,+){
            return -1
        }
        var res = 0
        var total = 0
        for i in 0..<cost.count{
            total+=gas[i]-cost[i]
            if total<0{
                total = 0
                res=i+1
            }
        }
        return res

    }
}
