class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n= s.length();
       boolean[] dp = new boolean[n+1];
       dp[n] =true;

       for(int i=n-1;i>=0;i--){
         for(String check:wordDict){
            int l = check.length();
            for(int j=0;j<check.length() && i+j<n;j++){
                if(check.charAt(j)==s.charAt(i+j)) l--;
            }
            if(l==0 && dp[i+check.length()]==true) dp[i]=true;
         }
       }
       for(int i=0;i<n;i++) System.out.println(dp[i]);
       return dp[0];
    }
}
