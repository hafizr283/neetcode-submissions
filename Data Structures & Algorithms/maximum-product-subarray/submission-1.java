class Solution {
    public int maxProduct(int[] nums) {
       int n=nums.length;
       boolean[] isComplete=new boolean[n+1];
       int[] dpmax = new int[n+1];
       int[] dpmin = new int[n+1];
       dpmax[0]=nums[0];
       dpmin[0]=nums[0];
       int ans = nums[0];
       for(int i=1;i<n;i++){
        int a = dpmax[i-1]*nums[i];
        int b= dpmin[i-1]*nums[i];
        int c = nums[i];
        
        dpmax[i]=Math.max(a,Math.max(b,c));
        dpmin[i]=Math.min(a,Math.min(b,c));
        ans = Math.max(dpmax[i],ans);
       }
       return ans;

               
    }
   
}
