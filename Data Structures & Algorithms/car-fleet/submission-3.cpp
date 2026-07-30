class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int,int>>v;
       for(int i=0;i<position.size();i++){
            v.push_back({position[i],speed[i]});
        }
        sort(v.begin(),v.end());
        vector<float>arr;
        for(auto item:v) arr.push_back(float(target-item.first)/item.second);
        int ans = 0;
        // reverse(arr.begin(),arr.end());
        for(auto item:arr) cout<<item<<' ';
        int max = -1;
        for(int i=arr.size()-1;i>0;i--){
            if(arr[i]-arr[i-1]>=0){
                arr[i-1]=arr[i];
            }
            else ans++;
        }
        return ans+1;
    }
};
