class Solution {
    private int max_len = 0;
    private int start = 0;
    public String longestPalindrome(String s) {
        int l = s.length();
        int dp[][] = new int[l][l];
        for (int i = 0; i < l; i++) {
            Arrays.fill(dp[i], -1);
        }
        for(int i=0;i<l;i++){
            for(int j=i;j<l;j++){
                if(dp[i][j]==-1) palindrome(dp,s,i,j);
                if(dp[i][j]==0) continue;
                int currentLength = j-i+1;
                if(currentLength>max_len){
                    max_len=currentLength;
                    start = i;
                }

            }
        }
        
        if(max_len>0) return s.substring(start,start+max_len);
        return "";
    }
    public int palindrome(int dp[][], String s, int i, int j) {
        if(dp[i][j]!=-1) return dp[i][j];
        if (i == j)
            return dp[i][i] = 1;
        if (j - i == 1)
            return dp[i][j] = (s.charAt(i) == s.charAt(j))?1:0;
        return dp[i][j] = (s.charAt(i)== s.charAt(j)?1:0) * palindrome(dp,s,i + 1, j - 1);
    }
}
