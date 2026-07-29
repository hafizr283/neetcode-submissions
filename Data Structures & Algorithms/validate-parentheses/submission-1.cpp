class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        bool ok=true;
        for(auto item:s){
            if(item=='(' or item=='{' or item=='[') st.push(item);
            else {
                if(st.empty()) return false;
                char ch = st.top();
                if(ch=='(' and item==')' or ch=='{' and item=='}' or ch=='[' and item==']'){
                    st.pop();
                }
                else return false;
            }
        }
        return st.empty()?true:false;
    }
};
