class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int ans = 0;
        stack<int>next_min;
        stack<int>prev_min;
        heights.push_back(0);
        int n = heights.size();
        vector<int>prev(n);

        
        // cout<<prev[3]<<' '<<prev[4]<<endl;
        for(int i=0;i<n;i++){
             while(!next_min.empty() and heights[next_min.top()]>heights[i]){
                int right = i;
                int h=heights[next_min.top()];
                next_min.pop();
                int left = next_min.empty()?-1:next_min.top();
                ans = max(ans, (right-left-1)*h);
            }
            next_min.push(i);
        }

        
        
        return ans;
    }
};
