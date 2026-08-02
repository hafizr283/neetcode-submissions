class TimeMap {
public:
unordered_map<string,vector<pair<int,string>>>mp;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        mp[key].push_back({timestamp,value});
    }
    
    string get(string key, int timestamp) {
        const auto& v = mp[key];
        int l = -1,r=v.size();
        while(r-l>1){
            int mid = midpoint(l,r);
            if(v[mid].first>timestamp) r=mid ;
            else l=mid; 
        }
        if(l==-1) return "";
        return v[l].second;
    }
};
