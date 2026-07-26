class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> temp;
        vector<vector<int>>ans;
        vector<int>v;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++){
            int left=i+1;
            int right = nums.size ()-1;
            while(left<right){
                while(left<right and i==left) {
                    left++; 
                }
                while(left<right and i==right) {
                    right--;
                }
                while(left<right and (nums[right]+nums[left]+nums[i])>0) right--;
                while(left<right and (nums[right]+nums[left]+nums[i])<0) left++;
                if(left<right and (nums[right]+nums[left]+nums[i])==0)  {
                    vector<int>triplet = {nums[right],nums[left], nums[i]};
                    sort(triplet.begin(),triplet.end());
                    temp.insert(triplet);
                    left++;right--;}

            }
        }
        for(auto it:temp){
            ans.push_back(it);
        }
        return ans;

        
        
    }
    
};
