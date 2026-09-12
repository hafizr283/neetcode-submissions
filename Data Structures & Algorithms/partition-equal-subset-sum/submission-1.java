class Solution {
    public boolean canPartition(int[] nums) {
       // i porjonto value gulo consider kore amount sum banano sube ki non-sealed
        int n = nums.length;
        int sum = 0;
        for(int value:nums) sum+=value;
        if(sum%2==1) return false;
        int target = sum/2;
        int[][] dp = new int[n][target+1];
        for(int[] row:dp)
            Arrays.fill(row,-1);
        return makeSum(n-1,sum/2,nums,dp);
    }
    private boolean makeSum(int i,int amount,int[] nums,int[][] dp){
        
        if(amount==0) {
            
            return true;
            }
        if(amount<0 || i<0) {
        
            return false;
        }
        if(dp[i][amount]!=-1) return dp[i][amount]==1;

        boolean x =  makeSum(i-1,amount,nums,dp) || makeSum(i-1,amount-nums[i],nums,dp);
        if(x==true) dp[i][amount]=1;
        else dp[i][amount]=0;
        return x;
    }
}
