class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       int ct_z=0;
       for(auto v:nums){
        if(v==0) ct_z++;
       }
         vector<int>ans(nums.size(),0);

       if(ct_z>=2){
         return ans;
       }
       if(ct_z==1){
         int prod=1;
         for(int i=0;i<nums.size();i++){
            if(nums[i]!=0) {
                prod*=nums[i];
                ans[i]=0;
            }

         }
         for(int i=0;i<nums.size();i++){
            if(nums[i]==0) ans[i]=prod;
         }
         return ans;

       }
        int prod = 1;
       for(int i=0;i<nums.size();i++){
        prod*=nums[i];

       }
       for(int i=0;i<nums.size();i++){
        ans[i]=prod/nums[i];
       }
       return ans;

    }
};
