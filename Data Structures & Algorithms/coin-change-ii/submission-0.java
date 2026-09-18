class Solution {
    public int change(int amount, int[] coins) {
     int n= coins.length;
     int[][] dp = new int[amount+1][n+1];
     for(int[] x:dp) Arrays.fill(x,-1);
     return chan(amount,coins,0,dp);
    }
    private int chan(int amount,int[] coins,int idx,int[][] dp){
        if(amount==0) return 1;
        if(amount<0) return 0;
        if(dp[amount][idx]!=-1) return dp[amount][idx];
        int sum=0;
        for(int i=idx;i<coins.length;i++){
            sum+=chan(amount-coins[i],coins,i,dp);
        }
        return dp[amount][idx]= sum;
    }
    
}
