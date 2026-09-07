class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
       boolean[][] dp=new boolean[n][n];
       int ans = 0;
       for(int l=1;l<=n;l++){
        for(int i=0;i<n-l+1;i++){
            int j=i+l-1;
            if(l==1) dp[i][j]=true;
            if(l==2 && s.charAt(i)==s.charAt(j)) dp[i][j]=true;
            if(l>2 && s.charAt(i)==s.charAt(j) && dp[i+1][j-1]==true) dp[i][j]=true;
            if(dp[i][j]==true)  ans++;
        }
       }

    return ans;
    }
}
