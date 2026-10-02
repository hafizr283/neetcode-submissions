class Solution {
    func isNStraightHand(_ hand: [Int], _ groupSize: Int) -> Bool {
        var freq = Dictionary<Int,Int>()
        for i in 0..<hand.count{
            freq[hand[i],default:0]+=1
        }

        let sortedCards = freq.keys.sorted()
        var g = groupSize
        for x in sortedCards{
            var current = freq[x]!
            if current<1{
                continue
            }
            
                for i in x..<x+g{
                freq[i,default:0]-=current;
                if freq[i]!<0{
                    return false
                }
            
            }
           
        }
        return true
    }
}
