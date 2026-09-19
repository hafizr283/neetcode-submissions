class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int l1 = s1.length();
        int l2 = s2.length();
        int l3 = s3.length();
        if(l3!=l1+l2) return false;
        Boolean[][] dp = new Boolean[l1+1][l2+1];
        return isI(s1,s2,s3,s1.length()-1,s2.length()-1,dp);
    }

    private boolean isI(String s1,String s2,String s3,int i,int j,Boolean[][] dp){
        if(i<0 && j<0) return true;
        if(dp[i+1][j+1]!=null) return dp[i+1][j+1];
        int k = i+j+1;
        boolean a=false;
        if(i>=0 && s1.charAt(i)==s3.charAt(k))
         a = isI(s1,s2,s3,i-1,j,dp);
         if(j>=0 && s2.charAt(j)==s3.charAt(k))
         a|=isI(s1,s2,s3,i,j-1,dp);
         return dp[i+1][j+1]=a;
    }
}
