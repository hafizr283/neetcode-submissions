class Solution {
    func jump(_ nums: [Int]) -> Int {
        var left=0
        var right = 0
        var ans = 0
        while right<nums.count-1{
            var farthest = 0
            for i in left...right{
                farthest=max(i+nums[i],farthest)
            }
            left = right+1
            right = farthest
            ans+=1
            

        }
        return ans

    }
}
