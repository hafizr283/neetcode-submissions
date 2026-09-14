class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int l1 = text1.length();
        int l2 = text2.length();
       int[][] dp = new int[l1+1][l2+1];
       for(int[] x:dp){
        Arrays.fill(x,-1);
       } 
       return commonSeq(l1-1,l2-1,text1,text2,dp);
    }
    private int commonSeq(int i,int j,String text1,String text2,int[][] dp){
        if(i<0 || j<0) return 0;
        if(dp[i][j]!=-1) return dp[i][j];
        int x = commonSeq(i-1,j,text1,text2,dp);
        int y = commonSeq(i,j-1,text1,text2,dp);
        int z = commonSeq(i-1,j-1,text1,text2,dp);
        if(text1.charAt(i)==text2.charAt(j)) z++;
        return dp[i][j]=Math.max(x,(Math.max(y,z)));
        


    }
}
