class Solution {
    public int lengthOfLIS(int[] nums) {
        int n=nums.length;
        int[] dp = new int[n+1];
        if(n==1) return 1;
        dp[0]=1;
        if(nums[1]>nums[0]) dp[1]=2;
        else dp[1]=1;
        int ans = Math.max(dp[0],dp[1]);
        for(int i=2;i<n;i++){
            int curr = 1;
            for(int j=0;j<i;j++){
                if(nums[j]<nums[i]){
                    curr = Math.max(curr,1+dp[j]);
                }

            }
            dp[i]=curr;
            ans = Math.max(curr,ans);
        }
        return ans;
    
        
    }
}
