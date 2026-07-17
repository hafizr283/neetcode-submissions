class Solution {
public:

    string encode(vector<string>& strs) {
        
        string str="";

        for(auto value: strs){
            int len = value.size();
            str+="_";
            str+=to_string(len);
            str+="_";
            str+=value;
            
        }
        cout<<str<<endl;
        
        return str;

    }

    vector<string> decode(string s) {
        vector<string>ans;
        int n= s.size();
        
        int i=0;
        while(i<n){
            string num ="0";
            int j=i;
            if(s[j]=='_') j++;
            while(isdigit(s[j])){
                num.push_back(s[j]);
                j++;
            }
            string temp = "";
            int nn= stoi(num);
            cout<<nn<<endl;
            int end = j+nn+1;
            j++;
            cout<<j<<' '<<end<<endl;
            while(j<end){
                temp.push_back(s[j]);
                j++;
            }
            ans.push_back(temp);
            i = j;

        }
        
        return ans;
    }

};
