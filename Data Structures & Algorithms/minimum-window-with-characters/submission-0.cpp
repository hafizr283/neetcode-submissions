class Solution {
public:
    string minWindow(string s, string t) {
        vector<int>hashs(60,0);
        vector<int>hasht(60,0);
        int left = 0;
        int ans = INT_MAX;
        pair<int,int> final_points;
        for(auto item:t) hasht[item-'A']++;
        int n = s.size();
        
        for(int right=0;right<n;right++){
            bool isvalid = 1;
            hashs[s[right]-'A']++;
            for(int i=0;i<60;i++){
                if(hashs[i]<hasht[i]){
                    isvalid=0;
                    break;         
                }
               
            }
            
             if(isvalid){
                cout<<left<<' '<<right<<endl;
            while(hashs[s[left]-'A']-1>=hasht[s[left]-'A']){
                hashs[s[left]-'A']--;
                left++;
            }
            if(right-left+1<ans){
                ans=right-left+1;
                final_points={left,right};
            }
        }
        }
       string ss="";
       cout<<ans<<endl;
       cout<<final_points.first<<' ';
        for(int i=final_points.first;i<=final_points.second;i++){
            ss.push_back(s[i]);
        }
        return ans==INT_MAX?"":ss;
    }
};
