class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        String s;
        generateP(2*n, "", 0, 0, ans);
        return ans;
    }
    private void generateP(int n, String s, int open, int close, List<String> ans) {
        if (open < close)
            return;
        if (n == 0) {
            if(open==close)
            ans.add(s);
            return;
        }

        generateP(n - 1, s + ')', open, close + 1, ans);
        generateP(n - 1, s + '(', open + 1, close, ans);
    }
}
