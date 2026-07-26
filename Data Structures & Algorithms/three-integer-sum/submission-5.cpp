class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> temp;
        vector<vector<int>>ans;
        vector<int>v;
        sort(nums.begin(),nums.end());
        //-2 0 0 2 2
        for(int i=0;i<nums.size();i++){
            if(i>0 and nums[i]==nums[i-1]) continue;
            int left=i+1;
            int right = nums.size ()-1;
            while(left<right){
                int sum = nums[i]+nums[left]+nums[right];
                if(sum==0) {
                    ans.push_back({nums[left],nums[i],nums[right]});
                    while(left<right and nums[left+1]==nums[left]) left++;
                    while(left<right and nums[right]==nums[right-1]) right--;
                    left++;
                    right--;
                }
                else if(sum<0) left++;
                else right--;

            }
        }
       
        return ans;

        
        
    }
    
};
