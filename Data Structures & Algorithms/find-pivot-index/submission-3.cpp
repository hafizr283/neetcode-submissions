class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n=nums.size();
        vector<int>pref(n,0);
        vector<int>suff(n,0);
        pref[0]=nums[0];
        for(int i=0;i<n;i++){
            if(i>0)
            pref[i]=pref[i-1]+nums[i];
           
        }
        for(int i=0;i<n;i++) cout<<pref[i]<<' ';

        suff[n-1]=nums[n-1];
        for(int i=n-2;i>=0;i--){
            suff[i]=suff[i+1]+nums[i];
        }
        for(int i=n-1;i>=0;i--) cout<<suff[i]<<' ';
        for(int i=0;i<n;i++){

            if(i>0 and i<n-1 and pref[i-1]==suff[i+1]) return i;
            if(i==0 and i+1<n and suff[i+1]==0) return i;
            if(n==1) return 0;
            if(i==(n-1) and i-1>=0 and pref[i-1]==0) return i;
        }
        return -1;
    }
};