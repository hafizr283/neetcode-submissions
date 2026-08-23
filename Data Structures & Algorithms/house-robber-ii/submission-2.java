class Solution {
    public int rob(int[] nums) {
       int n=nums.length;
       int[] dp1=new int[n+1];
       Arrays.fill(dp1,-1);
       if(n==1) return nums[0];
       if(n==2) return Math.max(nums[0],nums[1]);
       int x = func(0,n-2,dp1,nums);
       Arrays.fill(dp1,-1);
       int y = func(1,n-1,dp1,nums);
       
       return Math.max(x,y);
       

    }
    public int func(int l,int n,int[] dp,int[] arr){
        if(n==l) return arr[l];
        if(n==l+1) return Math.max(arr[l],arr[l+1]);
        if(dp[n]!=-1) return dp[n];
        return dp[n]=Math.max(arr[n]+func(l,n-2,dp,arr),func(l,n-1,dp,arr));
    }
}
