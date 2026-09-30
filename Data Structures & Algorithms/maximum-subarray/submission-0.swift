class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
     var  ans = nums[0];
     var localsum = 0;
     for i in 0..<nums.count{
        localsum=localsum+nums[i]
        ans=max(localsum,ans)
          if(localsum<0) {
            localsum=0
            
        }
     }
     return ans

    }
}
