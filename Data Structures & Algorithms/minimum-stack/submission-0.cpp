class MinStack {
    private: vector<int>v;
public:
    MinStack() {
        
        
    }
    
    void push(int val) {
        v.push_back(val);
    }
    
    void pop() {
        v.pop_back();
        
    }
    
    int top() {
        return v.back();
    }
    
    int getMin() {
        int mini = INT_MAX;
        for(auto item:v) mini = min(mini,item);
        return mini;
    }
};
