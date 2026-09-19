class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int n=nums.length;
        int sum = 0;
        for(int i=0;i<n;i++) sum+=nums[i];
        int[][] dp = new int[2*sum+1][n+1];
        for(int[] x:dp) Arrays.fill(x,-1);
        if(Math.abs(target)>sum) return 0;
        return findT(nums,target,nums.length-1,dp,sum);
        
    }
    private int findT(int[] nums,int target,int i,int[][] dp,int sum){
        if(i==-1) return target==0?1:0;
        // if(target<0) return 0;
        if(Math.abs(target)>sum) return 0;
        int idx = target+sum;
        if(dp[idx][i]!=-1) return dp[idx][i];
        return dp[idx][i]=findT(nums,target-nums[i],i-1,dp,sum)+findT(nums,target+nums[i],i-1,dp,sum);
    }
}
