class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
            
           int l = -1,r=matrix.size()*matrix[0].size();
           int n= r;
           int col_num = matrix[0].size();
           while(r-l>1){
            int mid = midpoint(l,r);
            if(matrix[mid/col_num][mid%col_num]<target){
                l=mid;
            }
            else {
                r=mid;
            }
           }
        if(r<n and matrix[r/col_num][r%col_num]==target){
            return true;

        }

        
        return false;
    }
};
