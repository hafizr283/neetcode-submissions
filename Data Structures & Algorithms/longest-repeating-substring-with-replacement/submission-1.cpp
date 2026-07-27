class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int>hash(27,0);
        int n = s.size();
        int left = 0,right =0;
        int mf = 0;
        int ans = 0;
        while(right<n){
            if(right-left-mf<=k){
                ans = max(ans,right-left);
                hash[s[right]-'A']++;
                mf = max(mf,hash[s[right]-'A']);
                right++;
            }
            else{
                hash[s[left]-'A']--;
                left++;
            }
        }
        if(right-left-mf<=k) ans = max(ans,right-left);
        return ans;
       
        
    }
};
