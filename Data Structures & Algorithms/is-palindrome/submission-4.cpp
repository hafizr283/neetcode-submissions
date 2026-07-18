class Solution {
public:
    bool isPalindrome(string s) {
        string final="";
        for(auto v:s){
            if((v>='a' and v<='z') or (v>='A' and v<='Z')) final.push_back(tolower(v));
            if(v>='0' and v<='9') final.push_back(v);
        }
        int n=final.size();
        cout<<n<<endl;
        cout<<final<<endl;
        for(int i=0;i<n/2;i++){
            if(final[i]!=final[n-i-1]) return false;
        }
        return true;
        
    }
};
