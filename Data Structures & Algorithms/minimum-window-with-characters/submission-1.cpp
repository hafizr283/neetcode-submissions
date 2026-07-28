class Solution {
public:
    string minWindow(string s, string t) {
      int formed = 0;
      unordered_map<char,int>need;
      unordered_map<char,int>have;
      for(auto v:t) need[v]++;
      int required = need.size();
      int left = 0;
      int n = s.size();
      int len =INT_MAX, start_index = -1;
      for(int right=0;right<n;right++){
        char ch = s[right];
        have[ch]++;
        if(need[ch] and have[ch]==need[ch]) formed++;
        while(formed==required){
            ch=s[left];
            have[ch]--;
            if(have[ch]<need[ch]) formed--;
            if(len>(right-left+1)){
                len = right-left+1;
                start_index = left;
            }
            left++;
        }
      }
      
      return start_index==-1?"":s.substr(start_index,len);
    }
};
