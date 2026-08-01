class Solution {
public:
    int score(vector<int>piles, int k){
        int ans = 0;
        for(auto item:piles) ans+=ceil(item*1.0/k); 
        return ans;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int l=1,r = *max_element(piles.begin(),piles.end());
        while(r-l>1){
            int mid = midpoint(l,r);
            if(score(piles,mid)>h) l = mid;
            else r=mid;
        }
        if(score(piles,l)<=h) return l;
        return r;
    }
};
