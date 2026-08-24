class Solution {
    public String longestPalindrome(String s) {
        String ans="";
        int len = 0;

        for (int i = 0; i < s.length(); i++) {
            int left = i, right = i;
            while (left >= 0 && right < s.length() && s.charAt(left)== s.charAt(right)) {
                 if (right - left + 1 > len) {
                    len = right - left + 1;
                    ans = s.substring(left, right + 1);
                }
                left--;
                right++;
               
            }
            left=i;
            right=i+1;
            while (left >= 0 && right < s.length() && s.charAt(left)== s.charAt(right)) {
                 if (right - left + 1 > len) {
                    len = right - left + 1;
                    ans = s.substring(left, right + 1);
                }
                left--;
                right++;
               
            }
            
        }
        return ans;
    }
}
