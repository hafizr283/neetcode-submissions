class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left=0,right=0;
        unordered_set<int>st;
        int ans  = 0;
        int n = s.size();
        while(left<=n-1 and right<=n-1){
            if(st.find(s[right])==st.end()){
                st.insert(s[right]);
                right++;
                ans = max(ans,int(st.size()));
                
            }
            else {
                ans = max(ans,int(st.size()));
                st.erase(s[left]);
                left++;
                
            }
        }
        return ans;
    }
};
