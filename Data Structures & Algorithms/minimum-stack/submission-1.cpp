class MinStack {
private: 
    stack<pair<int,int>>v;

public:
    MinStack() {
        
        
    }
    
    void push(int val) {
        if(!v.empty())
        {
            
            v.push({val,min(v.top().second,val)});
        }
        else 
         v.push({val,val});
    }
    
    void pop() {
        v.pop();
        
    }
    
    int top() {
        return v.top().first;
    }
    
    int getMin() {
        return v.top().second;
    }
};
