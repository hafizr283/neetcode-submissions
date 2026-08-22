

class Solution {
    public int rob(int[] cost) {
        int n=cost.length;
        int[] dp=new int[n+1];
        Arrays.fill(dp,-1);
        
        return func(cost,dp,n-1);
    }
    public int func(int[] cost,int[] dp,int n){
        if(dp[n]!=-1) return dp[n];
        if(n==0) return cost[n];
        if(n==1) return Math.max(cost[0],cost[1]);
        return dp[n]=Math.max(func(cost,dp,n-2)+cost[n],func(cost,dp,n-1));

    }
}

