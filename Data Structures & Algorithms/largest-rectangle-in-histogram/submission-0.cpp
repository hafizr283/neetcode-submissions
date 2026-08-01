class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int ans = 0;
        stack<int>next_min;
        stack<int>prev_min;
        heights.push_back(0);
        int n = heights.size();
        vector<int>prev(n);

        for(int i=n-1;i>=0;i--){
            while(!prev_min.empty() and heights[prev_min.top()]>heights[i]){
                prev[prev_min.top()]=i;
                prev_min.pop();
            }
            prev_min.push(i);
        }
        while(!prev_min.empty()){
            prev[prev_min.top()]=-1;
            prev_min.pop();
        }
        // cout<<prev[3]<<' '<<prev[4]<<endl;
        for(int i=0;i<n;i++){
             while(!next_min.empty() and heights[next_min.top()]>heights[i]){
                int width = i-prev[next_min.top()]-1;
                ans = max(ans,heights[next_min.top()]*width);
                next_min.pop();
            }
            next_min.push(i);
        }

        
        
        return ans;
    }
};
