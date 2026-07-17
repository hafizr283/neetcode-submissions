class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<long long, int>mp;
        int n = nums.size();
        for(auto v:nums) mp[v]++;
        int i=0;
        int result = 0;
        unordered_map<long long,int>ans;
        while(i<n){
            long long j=nums[i];
            int ct = 0;
            if(ans[j]!=0) {
                i++;
                continue; }
            while(mp[j]){
                j++;
                cout<<"siam"<<endl;
                
                ct++;
                ans[j]=ct;
            }
            result=max(result,ct);
            ans[nums[i]]=ct;
            i++;
        }
        return result;
        
    }
};
