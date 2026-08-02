class Solution {
public:
    int findMin(vector<int> &nums) {
        int right = nums.size()-1;
        int left = 0;
        while(right-left>1){
            int mid = midpoint(right,left);
            if(nums[mid]>nums[right]){
                left = mid;
            }
            else right = mid;
        }
        return min(nums[left],nums[right]);
    }
};
