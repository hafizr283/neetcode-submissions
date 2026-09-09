class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[] dp = new int[amount+1];
        Arrays.fill(dp,-1);
        int ans = minCoin(dp,coins,amount);
        if(ans==Integer.MAX_VALUE) return -1;
        return ans;
    }
    private int minCoin(int[] dp,int[] coins,int required){
        if(required==0) return 0;
        if(required<0) return Integer.MAX_VALUE;
        if(dp[required]!=-1) return dp[required];
        int mn = Integer.MAX_VALUE;
        for(int coin:coins){
            int val = minCoin(dp,coins,required-coin);
            if(val==Integer.MAX_VALUE) val = val - 1; 
           mn = Math.min(mn, 1+val);
        }
        return dp[required]=mn;
    }
}
