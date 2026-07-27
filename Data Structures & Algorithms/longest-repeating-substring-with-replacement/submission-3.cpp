class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int>hash(27,0);
        int n = s.size();
        int left = 0,right =0;
        int mf = 0;
        int ans = 0;
        for(;right<n;right++){
            hash[s[right]-'A']++;
            mf = max(mf,hash[s[right]-'A']);
            while(right-left+1-mf>k){
                hash[s[left]-'A']--;
                left++;
                
            } 
            ans=max(ans,right-left+1);
        }
        return ans;
       
        
    }
};
