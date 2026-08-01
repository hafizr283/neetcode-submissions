class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(auto v:matrix){
            int idx = lower_bound(v.begin(),v.end(),target)-v.begin();
            if(idx!=v.size() and v[idx]==target) return true;

        }
        return false;
    }
};
