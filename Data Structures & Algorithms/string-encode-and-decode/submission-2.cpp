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
        for(int i=0;i<n;i++){
            if(s[i]=='_'){
                string num = "";
                for(int j=i+1;j<n;j++){
                    if(isdigit(s[j])) num.push_back(s[j]);
                    else{
                        i=j;
                        break;
                    }
                }
                int nn=0;
                if(num.size()>0) nn= stoi(num);
                string temp="";
                for(int j=i+1;j<(i+1+nn);j++){
                    temp.push_back(s[j]);
                    
                }
                i=i+nn;
                
                ans.push_back(temp);
            }
        }
        
        return ans;
    }

};
