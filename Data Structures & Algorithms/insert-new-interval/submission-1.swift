class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        var new = newInterval
        var ans:[[Int]]=[]
        for i in 0..<intervals.count{
            var current = intervals[i]
            if current[1]<new[0]{
                ans.append(current)
            }
            else if new[1]<current[0]{
                ans.append(new)
                for j in i..<intervals.count{
                    ans.append(intervals[j])
                }
                return ans
            }
            else{
                new[0]=min(current[0],new[0])
                new[1]=max(current[1],new[1])
                
            }
        }
        ans.append(new)
        return ans

    }
}
