class Solution {
    public int numDecodings(String s) {
       int n = s.length();
       int[] dp=new int[n+1];
       Arrays.fill(dp,-1);
       dp[0]=1;
       return ways(n,dp,s);

    }
    public int ways(int i,int[] dp,String s){
        if(dp[i]!=-1) return dp[i];
        if(i==1 && s.charAt(0)=='0' ){
            return dp[i]=0;
        }
        else if(i==1) return dp[i]=1;
        int x=0,y=0;
        if(s.charAt(i-1)!='0') x=ways(i-1,dp,s);

         int val = Integer.parseInt(s.substring(i-2,i));
    if(val>9 && val<=26) y=ways(i-2,dp,s);
        
        return dp[i]=x+y; 
    }
}
