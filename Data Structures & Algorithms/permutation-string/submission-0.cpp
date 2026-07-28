class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int>f1(26,0);
        vector<int>f2(26,0);
        for(auto v:s1) f1[v-'a']++;
        for(int right=0;right<s2.size();right++){
            f2[s2[right]-'a']++;
            if(right-(int)s1.size()>=0) f2[s2[right-s1.size()]-'a']--;
            if(f1==f2) return true;
        }
        return false;
    }

};
