class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int>st;
        for(auto item:tokens){
            if(item=="+" or item=="-" or item=="/" or item=="*"){
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                if(item=="+") st.push(a+b);
                if(item=="-") st.push(a-b);
                if(item=="/") st.push(a/b);
                if(item=="*") st.push(a*b);
            }
            else{
                int x = stoi(item);
                st.push(x);
            }
        }
        return st.top();
    }
};
